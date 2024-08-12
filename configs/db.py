import os
from pymongo import MongoClient

DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_USERNAME = os.environ.get("DB_USERNAME")

MONGO_URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@todo-cluster.jxivs.mongodb.net/{DB_NAME}"

connection = MongoClient(MONGO_URI)

