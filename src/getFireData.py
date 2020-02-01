import requests

def getFireData():
    r = requests.get("https://api.breezometer.com/fires/v1/current-conditions?lat=&lon={longitude}&key=YOUR_API_KEY&radius={radius}")