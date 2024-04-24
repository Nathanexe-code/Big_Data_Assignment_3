#!/bin/bash

# Navigate to Kafka directory (Adjust path as necessary)
cd ~/Softwares/Kafka

# Start Zookeeper
echo "Starting Zookeeper..."
bin/zookeeper-server-start.sh config/zookeeper.properties > /dev/null 2>&1 &

sleep 5

# Start Kafka Server
echo "Starting Kafka server..."
bin/kafka-server-start.sh config/server.properties > /dev/null 2>&1 &

sleep 5

# Create Kafka topics if not already created
echo "Creating Kafka topics..."
bin/kafka-topics.sh --create --topic input --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 > /dev/null 2>&1
bin/kafka-topics.sh --create --topic output --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 > /dev/null 2>&1

# Navigate back to the project directory
cd ~/Work/Assigment_3

# Run Python scripts
echo "Running Producer script..."
python3 apriori.py &

echo "Running Consumer script..."
python3 pcy.py &

echo "All components are up and running."
