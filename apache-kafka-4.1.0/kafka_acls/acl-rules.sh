#!/bin/bash
set -e

# --- Configuration ---
# Set the absolute path for the Kafka binaries
KAFKA_BIN="/opt/kafka/bin"
BROKER="localhost:9094"
CONFIG_FILE="/etc/kafka/client.properties"
TOPIC_NAME="bbp-etl"
USER_NAME="mumtahina"

echo "========================================"
echo "Creating topic: $TOPIC_NAME"
echo "========================================"

$KAFKA_BIN/kafka-topics.sh \
  --bootstrap-server $BROKER \
  --command-config $CONFIG_FILE \
  --create \
  --topic $TOPIC_NAME \
  --partitions 1 \
  --replication-factor 1 || echo " Topic may already exist."

echo "========================================"
echo "Adding ACL for user: $USER_NAME"
echo "========================================"


$KAFKA_BIN/kafka-acls.sh \
  --bootstrap-server $BROKER \
  --command-config $CONFIG_FILE \
  --add \
  --allow-principal User:$USER_NAME \
  --operation Write \
  --topic $TOPIC_NAME


echo "ACL and topic setup complete!"