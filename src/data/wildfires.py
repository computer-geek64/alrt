import requests

def wildfires():
    url = "https://satepsanone.nesdis.noaa.gov/pub/FIRE/HMS/latesthmshysplit.txt"
    r = requests.get(url)
    data = r.text
    longitude = []
    latitude = []
    year = []
    date = []
    time = []
    duration = []
    statList = data.replace(" ", "").splitlines()
    for element in statList[1:]:
        element = element.split(",")
        longitude.append(element[0])
        latitude.append(element[1])
        year.append(element[2][:4])
        date.append(element[2][4:])
        time.append(element[3])
        duration.append(element[4])
    finaltup = (longitude, latitude, year, date, time, duration)
    return finaltup
