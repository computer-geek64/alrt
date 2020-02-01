from datetime import datetime
import requests
import json
import math
from config import GOOGLE_MAPS_API_KEY

def findPerson(person_latitude, person_longitude, person_altitude, person_velocity, disaster_type, last_time):
    if (disaster_type == "wildfire"):
        if (inBuilding(person_latitude, person_longitude)):
            return buildingRadius(last_time)
        else:
            return personRadius(last_time, person_velocity)
    if (disaster_type == "tsunami"):
        if (inBuilding(person_latitude, person_longitude)):
            tsunami_safe_altitude = 30 #in meters
            if (person_altitude > tsunami_safe_altitude):
                return 0
            return buildingRadius(person_latitude, person_longitude, last_time)
        else:
            return personRadius(last_time, person_velocity)
    if (disaster_type == "earthquake"):
        if (inBuilding(person_latitude, person_longitude, last_time)):
            return buildingRadius(last_time)
        else:
            return personRadius(last_time, person_velocity)
    if (disaster_type == "hurricane"):
        if (inBuilding(person_latitude, person_longitude)):
            return buildingRadius(last_time)
        else:
            return personRadius(last_time, person_velocity)
    if (disaster_type == "tornado"):
        if (inBuilding(person_latitude, person_longitude)):
            return buildingRadius(last_time)
        else:
            #average speed of running man 8.3 mph
            #average speed of running woman 6.5 mph
            #average of both 7.4mph
            current_time = datetime.now().timestamp()
            time_difference = current_time- last_time
            time_difference_in_hours = time_difference/3600
            average_running_speed = 7.4
            radius = time_difference_in_hours*average_running_speed
            return radius

def vectorAwayFromDisaster(person_latitude, person_longitude, disaster_latitude, disaster_longitude, radius):
    lat_change = (-1 * (disaster_latitude-person_latitude))*69.172 #in miles
    long_in_miles = math.cos(math.radians(person_latitude))*69.172
    long_change = (-1 * (disaster_longitude-person_longitude))*long_in_miles
    magnitude = math.sqrt(lat_change**2 + long_change**2)
    lat_change = lat_change*radius/magnitude
    long_change = long_change*radius/magnitude
    new_latitude = person_latitude+(lat_change/69.172)
    new_longitude = person_longitude+(long_change/(long_in_miles))
    disaster_point = [new_latitude, new_longitude]
    return disaster_point

def personAwayFromDisaster(person_old_lat, person_old_long, person_new_lat, person_new_long, radius):
    lat_change = -1 * (person_old_lat - person_new_lat)*69.172 #in miles
    long_in_miles = math.cos(math.radians(person_new_lat)) * 69.172
    long_change = -1 * (person_old_long - person_new_long)*long_in_miles #in miles
    magnitude = math.sqrt(lat_change**2 + long_change**2)
    lat_change = lat_change*radius/magnitude
    long_change = long_change*radius/magnitude
    new_latitude = person_new_lat+(lat_change/69.172)
    new_longitude = person_new_long+(long_change/long_in_miles)
    disaster_point = [new_latitude, new_longitude]
    return disaster_point

def buildingRadius(last_time):
    current_time = datetime.now().timestamp()
    time_difference = current_time - last_time
    time_difference_in_hours = time_difference/3600
    #average human speed = 15min per mile so 5mph
    average_speed = 5
    radius = time_difference_in_hours*average_speed
    return radius

def personRadius(last_time, person_velocity):
    current_time = datetime.now().timestamp()
    time_difference = current_time - last_time
    time_difference_in_hours = time_difference / 3600
    radius = time_difference_in_hours * person_velocity
    return radius

def inBuilding(person_latitude, person_longitude):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(person_latitude)+","+str(person_longitude)+"&key="+GOOGLE_MAPS_API_KEY)
    text = r.text
    data = json.loads(text)
    results = data["results"]
    for i in range(len(results)):
        list = results[i]['geometry']['location']
        print(list['lat'])
        print(list['lng'])
        if (abs(person_latitude-list['lat']) < 0.00005 and abs(person_longitude-list['lng']) < 0.00005):
            return True
    return False