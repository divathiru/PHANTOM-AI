from kafka import KafkaProducer
import json
from config import KAFKA_BROKER

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def publish_threat(threat):
    producer.send("cyber_threats", threat)
