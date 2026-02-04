# Imports.
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Environment variable reading.
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "test")


# Database connection setup and management.
class Database:
    def __init__(self):
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]

        self.collection = db["users"]

    def update_score(self, username: str, score: int):
        self.collection.update_one(
            {"username": username}, {"$inc": {"score", score}}, upsert=True
        )

    def get_top_scores(self):
        return list(self.collection.find().sort("score", -1))
