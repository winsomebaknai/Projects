from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["data_ingestion"]
transaction_col = db["transactions"]
system_logs_col = db["system_performance"]
user_activity_col = db["user_activity"]

#total spending per category
def total_spending_per_category():
    result = transaction_col.aggregate([
        {"$group": {"_id": "$category", "total_spent": {"$sum": "$amount"}}}
    ])
    return list(result)

#average spending per user
def avg_transaction_per_user():
    result = transaction_col.aggregate([
        {"$group" : {"_id" : "$user_id", "avg_amount" : {"$avg" : "$amount"}}}
    ])
    return list(result)

#average system performance
def avg_system_usage():
    result = system_logs_col.aggregate([
        {"$group": {"_id": "$device_id", "avg_cpu": {"$avg": "$cpu_usage"}, "avg_ram": {"$avg": "$ram_usage"}}}
    ])
    return list(result)

#devices with high CPU usage
def high_cpu_usage_devices():
    result = system_logs_col.find({"cpu_usage": {"$gt": 80}}, {"device_id": 1, "cpu_usage": 1, "_id": 0})
    return list(result)


#top visited websites by user
def top_visited_websites():
    result = user_activity_col.aggregate([
        {"$group": {"_id": "$url", "visit_count": {"$sum": 1}}},
        {"$sort": {"visit_count": -1}},
        {"$limit": 3}
    ])
    return list(result)

#most used browser
def most_used_browsers():
    result = user_activity_col.aggregate([
        {"$group": {"_id": "$browser", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    return list(result)

if __name__ == "__main__":
    print("Total Spending Per Category:", total_spending_per_category())
    print("Average Transaction Per User:", avg_transaction_per_user())
    print("Average System Usage:", avg_system_usage())
    print("Devices with High CPU Usage:", high_cpu_usage_devices())
    print("Top Visited Websites:", top_visited_websites())
    print("Most Used Browsers:", most_used_browsers())
