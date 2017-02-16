__author__ = 'rival'

from openweather import OpenWeather
from json import load
from io import open

config = load(open('config.json'))

APPID = config ["APPID"]

fetcher = OpenWeather(APPID)

def print_header(cities):
    print ("Достуные города:")

    for i,city in enumerate(cities):
        print("%d - %s" % (i+1, city["name"]))

cities = config["CITIES"]

print_header(cities)

city_index = int(input("Введите номер города: "))

city = cities[city_index-1]

city_id = city["id"]

result = fetcher.fetch_weather(city_id)

print ("%s: %.2f %s" % (city["name"], result.temperature, result.icon))
