from kafka import KafkaConsumer
import json

# Kafka SASL/PLAIN authentication configuration
bootstrap_servers = ['localhost:9092']
topic = 'bbp-etl'

# These credentials must match your JAAS config in the broker
sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_PLAINTEXT'
username = 'HITECH-CONSUMER'
password = 'HITECH-CONSUMER-secret'

# Create the consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    sasl_plain_username=username,
    sasl_plain_password=password,
    group_id='python-consumer-group',
    auto_offset_reset='earliest',  # consume from the beginning
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

print(f"✅ Listening for messages on topic: {topic}...")

try:
    for message in consumer:
        print("📩 Received message:")
        print(json.dumps(message.value, indent=2))
except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")
finally:
    consumer.close()
