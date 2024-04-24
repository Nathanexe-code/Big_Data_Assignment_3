from kafka import KafkaConsumer, KafkaProducer
import json
from apriori_module import frequent_item_sets, generate_rules  # assuming you saved the functions into apriori_module.py

# Kafka setup
consumer = KafkaConsumer(
    'check',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Consume messages
for message in consumer:
    transactions = message.value  # assuming each message is a list of transactions
    min_support = 2
    min_confidence = 0.5
    freq_sets = frequent_item_sets(transactions, min_support)
    rules = generate_rules(freq_sets, min_confidence)

    # Print or send the results
    print("Frequent Item Sets:", freq_sets)
    print("Association Rules:", rules)

    # Optionally send to another topic
    producer.send('results-topic', {'frequent_sets': freq_sets, 'rules': rules})

producer.flush()
