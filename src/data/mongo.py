#!/usr/bin/python3
# mongo.py

import sys
sys.path.append("../")
import pymongo
from datetime import datetime
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


def add_disaster_documents(documents):
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    db = client["disasters"]
    for document in documents:
        disaster_collection = db[document["type"] + "es" if document["type"] == "tornado" else document["type"] + "s"]
        if len(list(disaster_collection.find(document))) == 0:
            disaster_collection.insert_one(document)
    client.close()


def cleanup_user(user, time_threshold=15 * 60):
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    db = client["users"]
    user_collection = db[user]
    user_collection.delete_many({"time": {"$lt": datetime.now().timestamp() - time_threshold}})
    client.close()


def cleanup_disaster(disaster, time_threshold=4 * 60 * 60 * 24 * 7):
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    db = client["disasters"]
    user_collection = db[disaster]
    user_collection.delete_many({"time": {"$lt": datetime.now().timestamp() - time_threshold}})
    client.close()
