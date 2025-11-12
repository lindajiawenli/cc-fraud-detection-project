from kafka import KafkaConsumer

consumer = KafkaConsumer('transactions', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True, group_id='my-group', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    transaction = message.value
    amount = transaction['amount']
    X_pred = [[amount]]
    y_pred = model.predict(X_pred)
    if y_pred[0] == -1:
        print(f'Fraudulent transaction detected: {transaction}')
