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

        self.user_collection = db["users"]

    def get_user(self, username: str):
        return self.user_collection.find_one({"username": username})

    def set_user(self, username: str, password: str):
        self.user_collection.insert_one(
            {"username": username, "password": password, "score": 0}
        )

    def update_score(self, username: str, score: int):
        self.user_collection.update_one({"username": username}, {"$inc": {score}})
