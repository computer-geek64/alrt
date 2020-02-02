#!/usr/bin/python3
# alert.py

import math
from data import mongo
from data import gdacs
from data import wildfires
import geopy.distance
import pymongo
from time import sleep
from datetime import datetime
from config import MONGODB_USER, MONGODB_PASS


def monitor_danger(time_threshold=5 * 60, distance_thresholds={"hurricanes": 200, "floods": 50, "wildfires": 50}):
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    users = client["users"]
    threshold_difference = datetime.now().timestamp() - time_threshold
    output = []
    for user in users.list_collection_names():
        results = list(users[user].find({"time": {"$gte": threshold_difference}}))
        if len(results) == 0:
            # Location off
            last_location = users[user].find().sort("time", pymongo.DESCENDING).limit(1)[0]
            disasters = client["disasters"]
            for disaster in disasters.list_collection_names():
                for x in disasters[disaster].find():
                    if (disaster == "earthquakes" and geopy.distance.distance((x["lat"], x["lon"]), (last_location["lat"], last_location["lon"])).mi < math.exp(x["magnitude"] / 1.01 - 0.13) * 1000 * 0.00062137) or (disaster != "earthquakes" and geopy.distance.distance((x["lat"], x["lon"]), (last_location["lat"], last_location["lon"])).mi < distance_thresholds[disaster]):
                        if x["time"] >= last_location["time"] - 60 * 60 * 24:
                            output.append({"user": user, "last_location": last_location, "disaster": x})
    client.close()
    return output


while True:
    gdacs.download_geojson()
    documents = gdacs.get_disasters() + wildfires.get_wildfires()
    mongo.add_disaster_documents(documents)
    client = pymongo.MongoClient("mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASS + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    for user in client["users"].list_collection_names():
        mongo.cleanup_user(user)
    for disaster in client["disasters"].list_collection_names():
        mongo.cleanup_disaster(disaster)
    db = client["alerts"]
    user_collection = db["users"]
    user_collection.delete_many({})
    danger = monitor_danger()
    if len(danger) > 0:
        user_collection.insert_many(danger)
    client.close()
    sleep(300)