from kafka import KafkaConsumer, KafkaProducer
import json
from itertools import combinations
from collections import defaultdict

# Kafka Configuration
bootstrap_servers = ['localhost:9092']
input_topic = 'input'
output_topic = 'output'
consumer = KafkaConsumer(input_topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# PCY Algorithm Parameters
support_threshold = 100
basket_size = 2
hash_table_size = 10000

# Initialize counts and hash table
item_counts = defaultdict(int)
hash_table = defaultdict(int)

def process_data(data):
    # Count items and hash pairs
    for basket in data:
        for item in basket:
            item_counts[item] += 1
        for item1, item2 in combinations(basket, basket_size):
            hash_index = (hash(item1) + hash(item2)) % hash_table_size
            hash_table[hash_index] += 1

    # Identify frequent items and pairs
    frequent_items = {item for item, count in item_counts.items() if count >= support_threshold}
    frequent_pairs = []
    for basket in data:
        basket = [item for item in basket if item in frequent_items]
        for item1, item2 in combinations(basket, basket_size):
            hash_index = (hash(item1) + hash(item2)) % hash_table_size
            if hash_table[hash_index] >= support_threshold:
                frequent_pairs.append((item1, item2))
    return frequent_pairs

# Consume messages from Kafka
for message in consumer:
    data = message.value
    frequent_pairs = process_data(data)
    for pair in frequent_pairs:
        producer.send(output_topic, value=pair)

producer.flush()
