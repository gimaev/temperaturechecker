__author__ = 'rival'

from urllib.request import urlopen
from json import loads

class OpenWeather:

    class WeatherResult:

        def __init__(self, temperature, icon):
            self.temperature = temperature
            self.icon = icon

        def parse(data):
            def parse_icon(label):
                index = label[:len(label)-1] #отсекли из "13n" последнюю "n"
                return OpenWeather.ICONS[index]

            decoded_data = data.decode("utf-8") #кодирует бинарити в юникод
            weather_info = loads(decoded_data) #делает строку в словарь
            #print(weather_info)
            temperature = weather_info["main"]["temp"] #достаём температуру из словаря
            icon_weather = weather_info["weather"][0]["icon"]
            icon = parse_icon(icon_weather)
            return OpenWeather.WeatherResult(temperature, icon)

    URL_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}&units=metric"
    ICONS = {"01": "☀️", "02": "🌤", "03": "⛅️", "04": "🌥", "09": "🌧", "10": "🌦", "11": "🌩", "13": "🌨", "50": "🌫"}

    def __init__(self, appid):
        self.appid = appid

    def fetch_weather(self, city):
        weather_url = OpenWeather.URL_TEMPLATE.format(city, self.appid) #задать город и эппайли
        respone = urlopen(weather_url).read() #читает инфу из URl_TEMPLATE
        return OpenWeather.WeatherResult.parse(respone)



