#!/bin/bash

# Wait for Kafka to be ready
sleep 10

# Create topics
kafka-topics --bootstrap-server kafka:29092 --create --topic bbp-etl --partitions 1 --replication-factor 1 --command-config /etc/kafka/admin.properties

# Add ACLs for producer1 -> bbp-etl
kafka-acls --bootstrap-server kafka:29092 --command-config /etc/kafka/admin.properties \
    --add --allow-principal User:producer1 \
    --operation Write --operation Describe \
    --topic bbp-etl

# Add ACLs for IPA-BIDA -> bbp-etl
kafka-acls --bootstrap-server kafka:29092 --command-config /etc/kafka/admin.properties \
    --add --allow-principal User:IPA-BIDA \
    --operation Write --operation Describe \
    --topic bbp-etl

# Add ACLs for IPA-HITECH -> bbp-etl-hitech
kafka-acls --bootstrap-server kafka:29092 --command-config /etc/kafka/admin.properties \
    --add --allow-principal User:IPA-HITECH \
    --operation Write --operation Describe \
    --topic bbp-etl-hitech


# List all ACLs
kafka-acls --bootstrap-server kafka:29092 --command-config /etc/kafka/admin.properties --list