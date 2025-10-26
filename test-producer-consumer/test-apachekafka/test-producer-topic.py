from kafka import KafkaProducer
import json
import time

# Create Kafka producer with SASL/PLAIN authentication
producer = KafkaProducer(
    bootstrap_servers=['localhost:9094'],  # Use the SASL listener port
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    security_protocol='SASL_PLAINTEXT',  # or 'SASL_SSL' if using SSL
    sasl_mechanism='PLAIN',
    sasl_plain_username='mumtahina',
    sasl_plain_password='mumtahina-1221'
)

topic = "bbp-etl-x"

print("Producing messages to Kafka topic:", topic)

for i in range(10):
    message = {"id": i, "message": f"Hello Kafka {i}"}
    producer.send(topic, message)
    print(f"Sent: {message}")
    time.sleep(1)  # small delay for readability

producer.flush()
print("✅ All messages sent successfully!")
