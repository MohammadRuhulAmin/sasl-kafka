from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from datetime import datetime
import time

# Configuration for authenticated producer
config = {
    'bootstrap_servers': ['localhost:9092'],
    'security_protocol': 'SASL_PLAINTEXT',
    'sasl_mechanism': 'PLAIN',
    'sasl_plain_username': 'IPA-HITECH',
    'sasl_plain_password': 'IPA-HITECH-secret',
    'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    'api_version': (0, 10, 1)
}

def send_message(producer, topic, message):
    try:
        # Add timestamp to message
        message['timestamp'] = datetime.now().isoformat()
        
        # Send the message
        future = producer.send(topic, message)
        result = future.get(timeout=60)
        print(f"✅ Message sent successfully to {topic}")
        print(f"Partition: {result.partition}, Offset: {result.offset}")
        print(f"Message: {message}")
        print("-------------------")
        
    except KafkaError as e:
        print(f"❌ Failed to send message: {str(e)}")

def main():
    try:
        # Create producer instance
        producer = KafkaProducer(**config)
        producer.partitions_for('bbp-etl-hitech') 
        print("📡 Connected to Kafka successfully!")
        # Sample messages
        messages = [
            {"id": 1, "status": "processing", "data": "Sample data 1"},
            {"id": 2, "status": "completed", "data": "Sample data 2"},
            {"id": 3, "status": "processing", "data": "Sample data 3"}
        ]
        
        # Send each message
        for message in messages:
            send_message(producer, 'bbp-etl-hitech', message)
            time.sleep(1)  
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        producer.close()
        print("🔒 Producer connection closed")

if __name__ == "__main__":
    main()