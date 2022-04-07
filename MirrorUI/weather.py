import requests
import json

from geotracker import *


class Weather:
    def __init__(self) -> None:
        api_key = "c952d2356d192376967582488a306668"
        lat = GeoTracker().getLatlng()[0]
        lon = GeoTracker().getLatlng()[1]
        self.url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    def getData(self):
        response = requests.get(self.url)
        return json.loads(response.text)

    def getTemp(self):
        data = self.getData()
        return f"{data['current']['temp']} °C"

    def getIcon(self):
        data = self.getData()
        return f"https://openweathermap.org/img/wn/{data['current']['weather'][0]['icon']}@2x.png"


if __name__ == "__main__":
    weather = Weather()
    print(weather.getTemp())