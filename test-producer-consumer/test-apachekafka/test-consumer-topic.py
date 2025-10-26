from kafka import KafkaConsumer
import json

# Create Kafka consumer with SASL/PLAIN authentication
consumer = KafkaConsumer(
    'bbp-etl',
    bootstrap_servers=['localhost:9094'],  # SASL listener port
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group-w',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    security_protocol='SASL_PLAINTEXT',  # or 'SASL_SSL' if using SSL
    sasl_mechanism='PLAIN',
    sasl_plain_username='mumtahina',
    sasl_plain_password='mumtahina-1221'
)

print("Listening to messages from topic: quickstart-eventsx")

for message in consumer:
    print(f"Received message: {message.value}")
