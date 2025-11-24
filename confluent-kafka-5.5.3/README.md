
## List All the Topics in kafka Broker:

```sh
docker exec -it 05dd720d0060 kafka-topics \
  --bootstrap-server kafka:29092 \
  --list
```
## All the Message of a sepecific topic
```sh
docker exec -it 05dd720d0060 kafka-console-consumer \
  --bootstrap-server kafka:29092 \
  --topic bbp-etl \
  --from-beginning
```

## List All the Kafka-Acls 

```sh
docker exec -it 46abba93a4a3 kafka-acls \
  --bootstrap-server kafka:29092 \
  --list
```

## Add a rule for kafka-acl bbp-etl topic user: dashboard

```sh
docker exec -it 46abba93a4a3 kafka-acls \
  --bootstrap-server kafka:29092 \
  --add \
  --allow-principal User:dashboard \
  --operation Write \
  --topic bbp-etl


  docker exec -it bc355650a057  kafka-acls \
  --bootstrap-server kafka:9092 \
  --command-config /etc/kafka/admin.properties \
  --add \
  --allow-principal User:dashboard \
  --operation Write \
  --topic my-logs


```

## Delete a Topic from Kafka

```sh
docker exec -it 46abba93a4a3 kafka-topics \
  --bootstrap-server kafka:29092 \
  --delete \
  --topic bbp-etl
```

##  Create topic Command 

```sh
docker exec -it 3d88b5675385 kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --topic bbp-etl \
  --partitions 1 \
  --replication-factor 1


```

## Get latest Zookeeper Cluster id (If kafka cluster gets shutdown anytime)

```sh
docker exec -it sasl-kafka-zookeeper-1 zookeeper-shell localhost:2181
get /cluster/id
rename bbp-kafka/confluent-kafka-5.5.3/zkafka_data/kafka/meta.properties
```