from kafka import KafkaProducer
import json
import time

TOPIC_NAME = "credit-card-transactions"

producer = KafkaProducer(
    bootstrap_servers=f"credit-card-stream-linda-linda-enrichment.i.aivencloud.com:15287",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for i in range(15):
    transaction = generate_transaction()
    producer.send(TOPIC_NAME, value=transaction)
    time.sleep(1)

producer.close()
