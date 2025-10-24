from kafka import KafkaProducer
import json
import time

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Your Kafka broker
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "quickstart-eventsx"

print("Producing messages to Kafka topic:", topic)

for i in range(10):
    message = {"id": i, "message": f"Hello Kafka {i}"}
    producer.send(topic, message)
    print(f"Sent: {message}")
    time.sleep(1)  # small delay for readability

producer.flush()
print("✅ All messages sent successfully!")