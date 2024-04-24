# Big_Data_Assignment_3
## Fundamental of Big Data Analysis Assignment 3

Here's a comprehensive README file tailored for your project setup, which you can save as `README.md` in your `~/Work/Assigment_3` directory. This README provides an overview of the project, detailed setup and usage instructions, and a rationale for the chosen technologies.

---

## Project Overview
This project demonstrates a real-time data processing system using Apache Kafka for message streaming and MongoDB for data storage. The system applies data mining algorithms (Apriori and PCY) to streaming data, aiming to find frequent itemsets in large datasets, such as transaction data.

## Technologies Used
- **Apache Kafka**: Used for its robust messaging capabilities, allowing for the scalable and fault-tolerant streaming of data.
- **Python**: Used to implement data processing algorithms and interact with Kafka.
- **MongoDB**: A NoSQL database chosen for its flexibility in handling large volumes of structured and unstructured data, which is ideal for dynamic insertion of the processing results.
- **Bash**: Used to script the initialization of system components, providing an automated way to start the project.

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.6 or higher
- Apache Kafka 2.6 or higher
- MongoDB 4.4 or higher
- `kafka-python`: Python library for Kafka
- `pymongo`: Python library for MongoDB

## Setup and Installation
1. **Install Apache Kafka**:
   - Download Kafka from `https://kafka.apache.org/downloads`.
   - Extract Kafka and configure as per the Kafka documentation.

2. **Install MongoDB**:
   - Follow the installation instructions for MongoDB from `https://www.mongodb.com/try/download/community`.

3. **Install Python Dependencies**:
   ```bash
   pip3 install kafka-python pymongo
   ```

4. **Configure Kafka Topics**:
   - Start Kafka services (Zookeeper and Kafka server).
   - Create necessary topics:
     ```bash
     bin/kafka-topics.sh --create --topic input --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     bin/kafka-topics.sh --create --topic output --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     ```

## Usage
To run the project, execute the provided Bash script which will start all required services and scripts:
```bash
./run_project.sh
```
This script will:
- Start Kafka Zookeeper and Server.
- Create Kafka topics if they are not already created.
- Run the Python scripts for producing and consuming messages.

## Data Flow
- Data is produced by `apriori.py` script, which sends processed data to Kafka.
- `pcy.py` consumes this data, processes it to find frequent itemsets, and stores the results in MongoDB.

## Design Choices
- **Apache Kafka** was chosen for its ability to handle high throughput and low latency processing of real-time data streams.
- **MongoDB** was selected due to its schema-less nature, which allows for flexibility in the types of data stored, and its powerful query capabilities, making it suitable for analytics.
- **Python** offers a vast ecosystem of libraries which facilitates the easy implementation of data processing algorithms and interaction with Kafka and MongoDB.

## Conclusion
This system is designed to efficiently process and analyze large streams of data in real-time. By integrating Apache Kafka with MongoDB, the system leverages the strengths of both platforms to provide insightful analytics rapidly.

---

### Final Steps:
- Save this content in a file named `README.md` within your `~/Work/Assigment_3` directory.
- Review and adjust any specifics related to paths or additional setup details you might have customized for your environment.

This README should help users understand and navigate your project effectively.
