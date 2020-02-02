#!/usr/bin/python3
# api.py

import os
import json
from datetime import datetime
from data import mongo
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, jsonify, redirect, request, render_template, url_for, safe_join


app = Flask(__name__, template_folder="templates")
app.config.from_object("config")

limiter = Limiter(app, key_func=get_remote_address)

# Home
@app.route(app.config["HOME"], methods=["GET"])
@limiter.limit("1/s")
def get_home():
    return "Welcome to " + app.config["API_NAME"] + "!", 200


# API Endpoint
@app.route(safe_join(app.config["HOME"], "api", "alrt", "v1"), methods=["GET"])
def api_endpoint():
    return "Welcome to " + app.config["API_NAME"] + "\'s endpoint!", 200


# Update Location
@app.route(safe_join(app.config["HOME"], "api", "alrt", "v1", "update_location"), methods=["POST"])
def update_location():
    data = json.loads(request.data.decode())
    user_data = {"lat": data["coords"]["latitude"], "lon": data["coords"]["longitude"], "time": data["timestamp"]}
    mongo.add_user_documents([user_data], "sample_user0")
    return "Success!", 200


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
