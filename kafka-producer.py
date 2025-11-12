from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for i in range(10):
    transaction = generate_transaction()
    producer.send('transactions', value=transaction)

producer.flush()
