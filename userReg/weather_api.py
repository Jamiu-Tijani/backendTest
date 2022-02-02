from urllib import request
import requests

def get_weather(query):
    location = str(query)
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=b1258084bae0418492c10250220102&q={}&aqi=no".format(location))
    return response.json()