import random
import json
import time
from datetime import datetime, timedelta

#Generate Batch Data (financial transactions)
def generate_transaction_data(n=100):
    categories = ['Groceries', 'Electronics', 'Clothing', 'Restaurants', 'Entertainment']

    transactions = []
    for _ in range(n):
        transactions.append({""
        "transaction_id" : random.randint(100000, 9999999),
        "user_id" : random.randint(1,10),
        "amount" : round(random.uniform(10, 500), 2),
        "category" :random.choice(categories),
        "timestamp" : (datetime.now() - timedelta(days=random.randint(1,30))).isoformat()})

        return transactions
    
#Generate streaming data (system performance log)
def generate_system_log_data(n=100):
    return {
        "timestamp" : datetime.now().isoformat(),
        "cpu_usage" : round(random.uniform(10, 90),2),
        "ram_usage" : round(random.uniform(1, 30), 2),
        "device_id" :f"device_{random.randint(1,5)}"
    }

#Generate streaming data (user activity log)
def generate_user_activity_log():
    websites = ['facebook.com', 'google.com', 'amazon.com', 'netflix.com', 'github.com']
    browsers = ['chrome', 'firefox', 'safari', 'edge']
    devices = ['iphone', 'android', 'mac', 'windows']

    return {
        "timestamp" : datetime.now().isoformat(),
        "user_id" : random.randint(1,10),
        "url" : random.choice(websites),
        "browser" : random.choice(browsers),
        "device_type" : random.choice(devices)
    }

#save batch data as JSON file
batch_data = generate_transaction_data()
with open("batch_transactions.json", "w") as f:
    json.dump(batch_data, f, indent = 4)

print("Batch data saved as batch_transactions.json")

#simulate streaming data
print("streaming system performance and user activity logs")
for _ in range(5):
    print(generate_system_log_data())
    print(generate_user_activity_log())
    time.sleep(1)

