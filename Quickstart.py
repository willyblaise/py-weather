# Import from the file
from weather import Weather
import sys

api_key = sys.argv[1]
city_name = input("What city's weather would you like? ")
print("What unit of measure for the weather?")
unit = input("> ")

# Create an instance of weather object
instance = Weather(api_key, unit)

# Make a dictionary filled with information about the city by this method
data = instance.getWeather(city_name)

# This is just an example of how you should be printing this
name = f'City Name: {data["name"]}'
if unit == "metric":
    notation = "C"
elif unit == "imperial":
    notation = "F"
else:
    notation = ""
temperature = f'Temperature: {round(data["temperature"])}°{notation}'
pressure = f'Pressure: {round(data["pressure"])} Pascal'
humidity = f'Humidity: {data["humidity"]} g.m-3'
weather_condition = f'Weather Condition: {data["description"]}'
wind_speed = f'Wind Speed: {data["wind_speed"]} m/s'
wind_direction = f'Wind Direction: {data["wind_direction"]}°'


print(f'{name} \n{temperature} \n{pressure} \n{humidity} \n{weather_condition} \n{wind_speed} \n{wind_direction}')
