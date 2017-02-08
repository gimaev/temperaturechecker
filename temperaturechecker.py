__author__ = 'rival'

from openweather import OpenWeather

APPID = "5674f56bbb7193db0988e4b2e2a0e926"

fetcher = OpenWeather(APPID)

city = input("Введите город: ")


result = fetcher.fetch_weather(city)

print ("Погода в городе %s %.2f %s" % (city, result.temperature, result.icon))
