import requests
from datetime import datetime, timedelta

# API key for OpenWeatherMap
API_KEY = "bf5dfdfae8848c9763983934045d2bb3"

# Location of interest
LOCATION = "Agra, Uttar Pradesh, India"

# Get weather data for yesterday
yesterday = datetime.now() - timedelta(days=1)
yesterday_date_str = yesterday.strftime("%Y-%m-%d")

url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={LOCATION}&lon={LOCATION}&dt={yesterday_date_str}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Extract relevant weather information
hourly_data = data["hourly"]  # Access hourly data
temperature = hourly_data[0]["temp"]  # Temperature for the first hour (approximately yesterday's temperature)
description = hourly_data[0]["weather"][0]["description"]  # Weather description for the first hour
humidity = hourly_data[0]["humidity"]  # Humidity for the first hour
wind_speed = hourly_data[0]["wind_speed"]

# Print the weather information in a readable format
print("Yesterday's Weather in", LOCATION)
print("----------------------------------")
print("Temperature:", temperature, "°C")
print("Description:", description)
print("Humidity:", humidity, "%")
print("Wind Speed:", wind_speed, "m/s")
