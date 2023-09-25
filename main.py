import os

from dotenv import load_dotenv
import requests

from util_functions import get_wind_direction, send_weather_notification


# Sets variables from .env as environment variables and saves them as python variables
load_dotenv()
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")

# API Docs: https://openweathermap.org/current
raw_weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&units=imperial&appid={API_KEY}").json()

# Use the current weather code from initial request to fetch the corresponding icon to use for the notification icon
current_icon_code = raw_weather_data["weather"][0]["icon"]
current_weather_icon = requests.get(f"https://openweathermap.org/img/wn/{current_icon_code}.png").content
with open('weather-icon.png', 'wb') as f:
    """
    Have to save icon as file so notifypy can use it
    """
    f.write(current_weather_icon)

# Extracts specific data points from raw weather data request
current_temp = raw_weather_data["main"]["temp"]
current_feels_like_temp = raw_weather_data["main"]["feels_like"]
current_humidity = raw_weather_data["main"]["humidity"]
current_wind_speed = raw_weather_data["wind"]["speed"]
current_wind_direction = get_wind_direction(raw_weather_data["wind"]["deg"])

send_weather_notification(current_temp, current_feels_like_temp, current_humidity, current_wind_speed,
                          current_wind_direction)

os.remove("./weather-icon.png")
