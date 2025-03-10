#ingest data into mongoDB using Pymongo

from pymongo import MongoClient
import json
import time
from Generate_mock_data import generate_system_log_data, generate_user_activity_log

client = MongoClient("mongodb://localhost:27017/")
db = client["data_ingestion"]
transaction_col = db["transactions"]
system_logs_col = db["system_performance"]
user_activity_col = db["user_activity"]

#Ingest batch data
def ingest_batch_data():
    with open("batch_transactions.json", 'r') as f:
        transactions = json.load(f)
        transaction_col.insert_many(transactions)
    print("Batch data ingested into MongoDB")

#Ingest streaming data
def ingest_streaming_data(n=5):
    for _ in range(n):
        system_log = generate_system_log_data()
        user_activity = generate_user_activity_log()

        system_logs_col.insert_one(system_log)
        user_activity_col.insert_one(user_activity)

        print("inserted", system_log)
        print("inserted", user_activity)
        time.sleep(1)


ingest_batch_data()
ingest_streaming_data()

