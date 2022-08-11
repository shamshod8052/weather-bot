import requests
from googletrans import Translator
import datetime as dt
import logging

translator = Translator()
def weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "d7b5d330c7c654d90809e7647ad6e6f6"
    city = city
    url = base_url + "appid=" + api_key + "&q=" + city
    try:
        r = requests.get(url).json()
        # lon = r['coord']['lon']
        # lat = r['coord']['lat']
        temp_kelvin = r['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        # feels_like_kelvin = r['main']['feels_like']
        # feels_like_celsius = r['main']['feels_like'] - 273.15
        wind_speed = r['wind']['speed']
        humidity = r['main']['humidity']
        description = translator.translate(r['weather'][0]['description'], src='en', dest='uz').text.capitalize()
        sunrise_time = dt.datetime.utcfromtimestamp(r['sys']['sunrise'] + r['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(r['sys']['sunset'] + r['timezone'])
        text = f"🌎 {city.capitalize()}: {description}\n" \
               f"🌡 Temperatura:  {temp_celsius:.1F} °C yoki {temp_kelvin:.2F} °F\n" \
               f"💨 Shamol tezligi: {wind_speed} m/s\n" \
               f"💦 Namlik: {humidity} %\n" \
               f"🌅 Quyosh chiqishi: {sunrise_time}\n" \
               f"🌄 Quyosh botishi: {sunset_time}\n"
        return text
    except:
        pass