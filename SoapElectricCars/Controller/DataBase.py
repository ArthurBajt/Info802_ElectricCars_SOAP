from pymongo import MongoClient
from pymongo.database import Database


mongo_uri: str = "mongodb://localhost:27017"
client: MongoClient = MongoClient(mongo_uri)
db: Database = client["Cars"]
