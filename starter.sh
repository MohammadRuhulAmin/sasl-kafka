rm -rf ./zkafka_data/kafka
rm -rf ./zkafka_data/zookeeper
docker-compose down -v
docker-compose up -d --force-recreate