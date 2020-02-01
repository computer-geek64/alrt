from datetime import datetime

def findPerson(person_latitude, person_longitude, disaster_latitude, disaster_longitude, disaster_type, last_time):
    if (disaster_type == "wildfire"):
        if (inBuilding(person_latitude, person_longitude)):
            return buildingRadius(person_latitude, person_longitude, last_time)
    if (disaster_type == "tsunami"):

    if (disaster_type == "earthquake"):

    if (disaster_type == "hurricane"):

    if (disaster_type == "tornado"):


def buildingRadius(person_latitude, person_longitude, last_time):
    current_time = datetime.now().timestamp()
    time_difference = current_time - last_time
    time_difference_in_hours = time_difference/3600
    #average human speed = 15min per mile so 5mph
    average_speed = 5
    radius = time_difference_in_hours*average_speed
    return radius

def inBuilding(person_latitude, person_longitude):

