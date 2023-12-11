import requests
from selectorlib import Extractor
import os


class Temperature:
    """ A scraper that uses a yml file to read the xpath of a value it needs to extract from the
        timeanddate.com/weather/ url"""
    """headers dictionary variable is needed to make python behave like a browser during scraping. Not needed for 
    this project, but can be useful for scraping other websites."""
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    def __init__(self, website, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")
        self.website = website

    def get(self):
        location = f"{self.country}/{self.city}"
        url = os.path.join(f"{self.website}{location}")
        r = requests.get(url, headers=self.headers)
        c = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')

        try:
            temperature = extractor.extract(c)['temp']
            temp = float(temperature.replace(' °C', ''))
            return temp
        except KeyError as e:
            print(f"Error extracting temperature: {e}")
            return None


if __name__ == '__main__':
    city = input("Enter city: ")
    local_temperature = Temperature(website='https://www.timeanddate.com/weather/', country='usa', city=city)
    print(local_temperature.get())
