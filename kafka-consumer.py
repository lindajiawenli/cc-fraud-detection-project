from kafka import KafkaConsumer

TOPIC_NAME = "credit-card-transactions"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=f"credit-card-stream-linda-linda-enrichment.i.aivencloud.com:15287",
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
