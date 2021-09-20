docker build -t flume-kafka .
docker run --network confluent -it flume-kafka