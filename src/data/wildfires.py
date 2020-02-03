#!/usr/bin/python3
# wildfires.py

import requests
from datetime import datetime


def get_wildfires():
    url = "https://satepsanone.nesdis.noaa.gov/pub/FIRE/HMS/latesthmshysplit.txt"
    response = requests.get(url)
    lines = response.text.replace(" ", "").strip().split("\n")[1:]
    output = []
    for line in lines:
        field = line.split(",")
        time = datetime.strptime(field[2] + field[3], "%Y%m%d%H%M").timestamp()
        output.append({"type": "wildfire", "lat": float(field[1]), "lon": float(field[0]), "time": time})
    return output
