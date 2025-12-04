from flask import current_app, g
from pymongo import MongoClient

def get_mongo_db():
    if "mongo_db" not in g:
        client = MongoClient(current_app.config["MONGO_URI"])
        g.mongo_client = client
        g.mongo_db = client[current_app.config["MONGO_DB_NAME"]]
    return g.mongo_db

def close_mongo(e=None):
    client = getattr(g, "mongo_client", None)
    if client is not None:
        client.close()
