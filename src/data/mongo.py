#!/usr/bin/python3
# mongo.py

import sys
sys.path.append("../")
import pymongo
from config import MONGODB_USER, MONGODB_PASS


def add_user_documents(documents, user):
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    db = client["users"]
    user_collection = db[user]
    user_collection.insert_many(documents)
    client.close()


def delete_user_documents(documents, user):
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    db = client["users"]
    user_collection = db[user]
    user_collection.delete_many(documents)
    client.close()
