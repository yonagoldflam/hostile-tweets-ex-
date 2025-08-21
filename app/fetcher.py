import os
import pymongo
from pymongo.errors import PyMongoError

class Connection:
    def __init__(self):
        self.collection_name = os.getenv("MONGODB_COLLECTION", "tweets")

        try:
            mongo_user = os.getenv("MONGODB_USER", "IRGC")
            mongo_password = os.getenv("MONGODB_PASSWORD", "iraniraniran")
            db_name = os.getenv("MONGODB_DATABASE", "IranMalDB")

            self.db_url = f"mongodb+srv://{mongo_user}:{mongo_password}@{db_name}.gurutam.mongodb.net/"

            self.client = pymongo.MongoClient(self.db_url)

            self.db = self.client[db_name]
        except PyMongoError as e:
            raise RuntimeError(f"MongoDB connection error: {e}")

        try:
            print(list(self.db[self.collection_name].find({}, {"_id": 0})))
        except PyMongoError as e:
            print({"error": f"database_error: {e}"})
c=Connection()

