import geocoder
from geopy.geocoders import Nominatim

class GeoTracker:
    def __init__(self) -> None:
        self.geolocator = Nominatim(user_agent="geoapiExercises")
        #print(type(self.geolocator))

    def getLatlng(self):
        g = geocoder.ip('me')
        return g.latlng

    def getCity(self):
        latlng = self.getLatlng()
        Latitude = latlng[0]
        Longitude = latlng[1]
        location = self.geolocator.reverse(f"{Latitude},{Longitude}")
        address = location.raw['address']
        return address.get('city', '')


if __name__ == "__main__":
    geo = GeoTracker()