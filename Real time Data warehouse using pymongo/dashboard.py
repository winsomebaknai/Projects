from flask import Flask
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["data_ingestion"]

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])


def fetch_data():
    transactions = list(db["transactions"].aggregate([
        {"$group": {"_id": "$category", "total_spent": {"$sum": "$amount"}}}
    ]))
    
    system_usage = list(db["system_performance"].aggregate([
        {"$group": {"_id": "$device_id", "avg_cpu": {"$avg": "$cpu_usage"}, "avg_ram": {"$avg": "$ram_usage"}}}
    ]))
    
    user_activity = list(db["user_activity"].aggregate([
        {"$group": {"_id": "$url", "visit_count": {"$sum": 1}}},
        {"$sort": {"visit_count": -1}},
        {"$limit": 5}
    ]))
    
    return transactions, system_usage, user_activity

transactions, system_usage, user_activity = fetch_data()

tx_df = pd.DataFrame(transactions)
sys_df = pd.DataFrame(system_usage)
ua_df = pd.DataFrame(user_activity)

tx_df = tx_df.rename(columns={"_id": "Category", "total_spent": "Total Spent"}) if not tx_df.empty else pd.DataFrame(columns=["Category", "Total Spent"])
sys_df = sys_df.rename(columns={"_id": "Device", "avg_cpu": "Avg CPU", "avg_ram": "Avg RAM"}) if not sys_df.empty else pd.DataFrame(columns=["Device", "Avg CPU", "Avg RAM"])
ua_df = ua_df.rename(columns={"_id": "Website", "visit_count": "Visit Count"}) if not ua_df.empty else pd.DataFrame(columns=["Website", "Visit Count"])


app.layout = dbc.Container([
    html.H1("Real-Time Data Warehouse Dashboard", className="text-center"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.bar(tx_df, x="Category", y="Total Spent", title="Total Spending Per Category")), width=6),
        dbc.Col(dcc.Graph(figure=px.bar(sys_df, x="Device", y="Avg CPU", title="Average CPU Usage Per Device")), width=6),
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.bar(ua_df, x="Website", y="Visit Count", title="Top Visited Websites")), width=6),
        dbc.Col(dcc.Graph(figure=px.bar(sys_df, x="Device", y="Avg RAM", title="Average RAM Usage Per Device")), width=6),
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=True)