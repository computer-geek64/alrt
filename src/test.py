#!/usr/bin/python3
# test.py

import gmplot
from data import mongo
from datetime import datetime

timestamp = datetime.now().timestamp() - 10 * 60
mongo.delete_user_documents({}, "sample_user0")
mongo.add_user_documents([{"lat": 29.640761, "lon": -82.353638, "time": timestamp}, {"lat": 29.640751, "lon": -82.353648, "time": timestamp - 120}, {"lat": 29.640741, "lon": -82.353658, "time": timestamp - 240}], "sample_user0")

#gmap = gmplot.GoogleMapPlotter(29.640761, -82.353638, 17)
#gmplot.GoogleMapPlotter(apikey="")
#gmap.circle(29.640761, -82.353638, 0.5 * 1609.34, "blue")
#gmap.marker(29.640761, -82.353638, "green")
#gmap.draw("test.html")