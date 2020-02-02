import requests

def getFireData():
    r = requests.get("https://api.breezometer.com/fires/v1/current-conditions?lat=&lon={longitude}&key=YOUR_API_KEY&radius={radius}")

def getTornadoData():
    r = requests.get("http://dataservice.accuweather.com/tropical/v1/gov/storms/active?apikey=GR7EQRyLZ9xunruEcLtLtpQvUNQwOXt7")
    print(r.text)
    return

getTornadoData()