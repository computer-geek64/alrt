#!/usr/bin/python3
# alert.py

import sys
sys.path.append("../")
import math
import mongo
import geopy.distance
import pymongo
from datetime import datetime
from config import MONGODB_USER, MONGODB_PASS


def monitor_danger(time_threshold=5 * 60, distance_thresholds={"tornadoes": 5, "hurricanes": 200, "floods": 50, "wildfires": 50}):
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
                    if (disaster == "earthquakes" and geopy.distance.distance((x["lat"], x["lon"]), (last_location["lat"], last_location["lon"])) < math.exp(x["magnitude"] / 1.01 - 0.13) * 1000 * 0.00062137) or geopy.distance.distance((x["lat"], x["lon"]), (last_location["lat"], last_location["lon"])) < distance_thresholds:
                        output.append({"user": user, "last_location": last_location, "disaster": x})
    client.close()
    return output

print(monitor_danger())