import json
import os
from kafka import KafkaProducer

folderName = "C:/Users/mgupt/Desktop/KafkaDemo/env/"
producer = KafkaProducer(
    bootstrap_servers="kafka-demo-manvigupta226-fbca.c.aivencloud.com:28258",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)

producer.send("test-topic",
                key={"key": 1},
                value={"message": "hello world"}
            )
producer.flush()            