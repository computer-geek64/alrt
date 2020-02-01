#!/usr/bin/python3
# gdacs.py

import os
import json
from subprocess import Popen
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def download_geojson():
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile("/root/.mozilla/firefox/hct90kvg.selenium")
    browser = webdriver.Firefox(firefox_profile=profile, options=options)
    browser.get("https://gdacs.org/Alerts/default.aspx")
    browser.find_element_by_id("iconDownload").click()
    browser.close()
    Popen(["mv", "/root/Downloads/result.geojson", "."])
    return os.path.dirname(__file__)


def get_disasters(filename, limit):
    with open(filename, "r") as file:
        geojson = json.loads(file.read())
    disasters = []
    i = 0
    while len(disasters) < limit:
        if geojson["features"][i]["properties"]["eventtype"] == "EQ":
            # Earthquake
            disasters.append({
                "type": "earthquake",
                "lat": geojson["features"][i]["properties"]["latitude"],
                "lon": geojson["features"][i]["properties"]["longitude"],
                "from": datetime.strptime(geojson["features"][i]["properties"]["fromdate"], "%d/%b/%Y %H:%M:%S").timestamp(),
                "to": datetime.strptime(geojson["features"][i]["properties"]["todate"], "%d/%b/%Y %H:%M:%S").timestamp()
            })
        elif geojson["features"][i]["properties"]["eventtype"] == "FL":
            # Flood/Tsunami
            disasters.append({
                "type": "Flood",
                "lat": geojson["features"][i]["properties"]["latitude"],
                "lon": geojson["features"][i]["properties"]["longitude"],
                "from": datetime.strptime(geojson["features"][i]["properties"]["fromdate"], "%d/%b/%Y %H:%M:%S").timestamp(),
                "to": datetime.strptime(geojson["features"][i]["properties"]["todate"], "%d/%b/%Y %H:%M:%S").timestamp()
            })
        elif geojson["features"][i]["properties"]["eventtype"] == "TC":
            # Tropical Cyclone/Hurricane
            disasters.append({
                "type": "Tropical Cyclone/Hurricane",
                "lat": geojson["features"][i]["properties"]["latitude"],
                "lon": geojson["features"][i]["properties"]["longitude"],
                "from": datetime.strptime(geojson["features"][i]["properties"]["fromdate"], "%d/%b/%Y %H:%M:%S").timestamp(),
                "to": datetime.strptime(geojson["features"][i]["properties"]["todate"], "%d/%b/%Y %H:%M:%S").timestamp()
            })
        i += 1
    return disasters

print(get_disasters("result.geojson", 5))