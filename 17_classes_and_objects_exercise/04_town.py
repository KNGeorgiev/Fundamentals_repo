class Town:

    def __init__(self, name: str):
        self.name = name

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return_text = f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
        return return_text


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
