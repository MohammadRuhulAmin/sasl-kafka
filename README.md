

# KAFKA-ACL
- Create Topic, with authorization
```sh
bin/kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --command-config /etc/kafka/client.properties \
    --create \
    --topic bbp-etl \
    --partitions 1 \
    --replication-factor 1

```
- Allow Write permission

```sh
bin/kafka-acls.sh \
    --bootstrap-server localhost:9094 \
    --command-config /etc/kafka/client.properties \
    --add \
    --allow-principal User:mumtahina \
    --operation Write \
    --topic bbp-etl-x

```