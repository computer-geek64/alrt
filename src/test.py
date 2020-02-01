#!/usr/bin/python3
# test.py

from data import mongo


mongo.delete_user_documents({}, "sample_user0")