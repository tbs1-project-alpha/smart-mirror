import requests
import json

from MirrorUI.geotracker import *


class Weather:
    def __init__(self) -> None:
        api_key = "API_KEY"
        fallback_location = (51.4709935, 7.1555183)

        try:
            geotracker = GeoTracker()
            lat, lon = geotracker.getLatlng()
        except:
            lat, lon = fallback_location
            
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


# if __name__ == "__main__":
#     weather = Weather()
#     print(weather.getTemp())