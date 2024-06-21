
import requests
import json

print("Type any city to get a weather update.")
city_name = input("City Name: ")

API_key = "4a0028eafa55b4fd4623aa832dd70bbb"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    for item in weather_data['list']:
        timestamp = item['dt_txt']
        temperature = item['main']['temp']
        feels_like = item['main']['feels_like']
        description = item['weather'][0]['description']
        wind_speed = item['wind']['speed']
        print(f"At {timestamp}:")
        print(f"  Temperature: {temperature} K")
        print(f"  Feels like: {feels_like} K")
        print(f"  Description: {description}")
        print(f"  Wind speed: {wind_speed} m/s")
        print()
else:
    print(f"Error fetching data: {response.status_code} - {response.reason}")


