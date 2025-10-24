from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    'quickstart-eventsx',
    bootstrap_servers=['localhost:9094'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group-w',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Listening to messages from topic: quickstart-events")

for message in consumer:
    print(f"Received message: {message.value}")