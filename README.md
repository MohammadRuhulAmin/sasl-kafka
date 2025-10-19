
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
docker exec -it 05dd720d0060 kafka-acls \
  --bootstrap-server kafka:29092 \
  --list
```

## Add a rule for kafka bbp-etl topic user: dashboard

```sh
docker exec -it 05dd720d0060 kafka-acls \
  --bootstrap-server kafka:29092 \
  --add \
  --allow-principal User:dashboard \
  --operation Write \
  --topic bbp-etl

```