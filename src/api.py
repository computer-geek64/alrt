#!/usr/bin/python3
# api.py

import os
import json
import math
import pymongo
from datetime import datetime
from data import mongo
from data import predict
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, jsonify, redirect, request, render_template, url_for, safe_join


app = Flask(__name__, template_folder="templates")
app.config.from_object("config")

limiter = Limiter(app, key_func=get_remote_address)

# Home
@app.route(app.config["HOME"], methods=["GET"])
def get_home():
    return "Welcome to " + app.config["API_NAME"] + "!", 200


# API Endpoint
@app.route(safe_join(app.config["HOME"], "api", "alrt", "v1"), methods=["GET"])
def api_endpoint():
    return "Welcome to " + app.config["API_NAME"] + "\'s endpoint!", 200


# Update Location
@app.route(safe_join(app.config["HOME"], "api", "alrt", "v1", "update_location"), methods=["POST"])
@limiter.limit("1/second")
def update_location():
    data = json.loads(request.data.decode())
    user_data = {"lat": data["coords"]["latitude"], "lon": data["coords"]["longitude"], "time": data["timestamp"] / 1000}
    mongo.add_user_documents([user_data], "sample_user0")
    return "Success!", 200


# Get users in danger
@app.route(safe_join(app.config["HOME"], "api", "alrt", "v1", "get_users"), methods=["GET"])
def get_users():
    client = pymongo.MongoClient("mongodb+srv://" + app.config["MONGODB_USER"] + ":" + app.config["MONGODB_PASS"] + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    db = client["alerts"]
    user_collection = db["users"]
    results = list(user_collection.find())
    client.close()
    return jsonify(results), 200


# Get plotting coordinate points
@app.route(safe_join(app.config["HOME"], "api", "alrt", "v1", "points", "<string:user>"), methods=["GET"])
def get_points(user):
    client = pymongo.MongoClient("mongodb+srv://" + app.config["MONGODB_USER"] + ":" + app.config["MONGODB_PASS"] + "@alrt-ypzt7.mongodb.net/test?retryWrites=true&w=majority")
    data = list(client["alerts"]["users"].find())
    results = [x["user"] for x in data]
    if user in results:
        data = data[results.index(user)]
        db = client["users"]
        user_collection = db[user]
        results = list(user_collection.find().sort("time", pymongo.ASCENDING))
        x = []
        y = []
        for result in results:
            x.append(result["lat"])
            y.append(result["lon"])
        time_elapsed = (datetime.now().timestamp() - data["last_location"]["time"]) / 60 / 60
        radius = 4 * time_elapsed - (2 ** (time_elapsed / 4 - 2)) / math.log(2) + 1 / (4 * math.log(2))
        predicted_point = predict.predict_point(x, y, radius, (data["disaster"]["lat"], data["disaster"]["lon"]))
        json_response = {"disaster": [{"latitudeP": predicted_point[0], "longitudeP": predicted_point[1], "latitudeL": x[-1], "longitudeL": y[-1], "latitudeD": data["disaster"]["lat"], "longitudeD": data["disaster"]["lon"], "radius": radius}]}
        client.close()
        return jsonify(json_response), 200
    results = client["users"][user].find().sort("time", pymongo.DESCENDING).limit(1)[0]
    client.close()
    return jsonify({"disaster": [{"latitudeL": results["lat"], "longitudeL": results["lon"]}]}), 200

# Error handlers
@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404


@app.errorhandler(400)
def error_400(e):
    return "HTTP 400 - Bad Request", 400


@app.errorhandler(500)
def error_500(e):
    return "HTTP 500 - Internal Server Error", 500


if __name__ == "__main__":
    app.run(app.config["IP"], app.config["PORT"])
