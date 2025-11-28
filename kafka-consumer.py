from kafka import KafkaConsumer
from define_model import model
from dotenv import load_dotenv
import os

load_dotenv()

TOPIC_NAME = "credit-card-transactions"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=os.getenv("KAFKA_SERVICE_URI"),
    client_id = "CONSUMER_CLIENT_ID",
    group_id = "CONSUMER_GROUP_ID",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for message in consumer:
    transaction = message.value
    amount = transaction['amount']
    X_pred = [[amount]]
    y_pred = model.predict(X_pred)
    if y_pred[0] == -1:
        print(f'Fraudulent transaction detected: {transaction}')
