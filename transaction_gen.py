from faker import Faker
import random

fake = Faker()

def generate_transaction():
    return {
        "timestamp": fake.date_time_this_month().strftime("%Y-%m-%d %H:%M:%S"),
        "card_number": fake.credit_card_number(),
        "amount": round(random.uniform(1, 10000), 2)
    }

for i in range(15):
    print(generate_transaction())
