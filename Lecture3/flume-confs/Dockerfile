FROM probablyfine/flume

ADD kafka-to-file.conf /var/tmp/kafka-to-file.conf

RUN mkdir -p ./kafka-files-new

ENTRYPOINT [ "flume-ng", "agent", "-c", "/opt/flume/conf", "-f", "/var/tmp/kafka-to-file.conf", "-n", "KafkaFileAgent", "-Dflume.root.logger=INFO,console" ]
