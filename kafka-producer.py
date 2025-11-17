from kafka import KafkaProducer
import json
import time

from transaction_gen import generate_transaction

TOPIC_NAME = "credit-card-transactions"

producer = KafkaProducer(
    bootstrap_servers=f"credit-card-stream-linda-linda-enrichment.i.aivencloud.com:15287",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

try:
	for i in range(100):
    		transaction_dictionary = generate_transaction()
    		transaction_bytes = json.dumps(transaction_dictionary).encode("utf-8")
    		producer.send(TOPIC_NAME, value=transaction_bytes)
	
	producer.flush()
	print("\nAll 100 messages sent successfully")

except Exception as e:
	print("Error: {e}")

finally:
	producer.close()
	print("Producer closed")
