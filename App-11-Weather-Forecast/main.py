import requests, pprint


class Weather:

    def __init__(self, api_key, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise AttributeError("")

    def next_12_h(self):
        result = self.data['list'][:4]
        return result

    def next_12_h_simplified(self):
        pass


city = input("Enter the city: ").title()
api_key = "525edac8c50454f21c9557e48d9a893e"

weather = Weather(api_key=api_key, city=city)
pprint.pprint(weather.next_12_h())
