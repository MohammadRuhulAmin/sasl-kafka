from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from datetime import datetime
import time

# Configuration for authenticated producer
config = {
    'bootstrap_servers': ['10.10.200.72:9092'],#['172.16.48.88:9092'],
    'security_protocol': 'SASL_PLAINTEXT',
    'sasl_mechanism': 'PLAIN',
    'sasl_plain_username': 'dashboard',
    'sasl_plain_password': '$$xdsx12!!@@33Xsd',
    'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    'api_version': (0, 10, 1)
}

def send_message(producer, topic, message):
    try:
        # Add timestamp to message
        message['timestamp'] = datetime.now().isoformat()
        future = producer.send(topic, message)
        result = future.get() #timeout=60
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
        producer.partitions_for('bbp-etl') 
        print("📡 Connected to Kafka successfully!")
        # Sample messages
        messages = [
            {
            "jobId": "9e50834b-6374-46fa-9581-cc6394c2fa6f",
            "scheduleId": "e7350603-24d0-4c50-b9ef-23bb026f3edb",
            "scheduleName": "Test Every 6 Minute",
            "reportType": "null",
            "status": "null",
            "timestamp": "null",
            "createdBy": "null",
            "ipaRole": "all",
            "recipients": "{}",
            "params":"{}"
}
        ]
        
        # Send each message
        for message in messages:
            send_message(producer, 'bbp-etl', message)
            time.sleep(1)  
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        producer.close()
        print("🔒 Producer connection closed")

if __name__ == "__main__":
    main()