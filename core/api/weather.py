from core.utils.restapi import RequestsAPI


## constants
WEATHER_API_KEY = "946cf08edb214516a58145535241206"

class WeatherApi():
    def __init__(self):
    
        self.weather = RequestsAPI("https://api.weatherapi.com")


    def get_weather_byzip(self, city):
        response = self.weather.get("/v1/current.json", params={'q': city, 'lang': 'en', 'key': WEATHER_API_KEY})
        return response.json()
    
    def forecast_weather(self, days,city):
        response = self.weather.get("/v1/forecast.json", params={'q': city, 'days': days, 'lang': 'en', 'key': WEATHER_API_KEY})
        return response.json()