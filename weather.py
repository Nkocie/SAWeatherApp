import requests

# Your API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY_HERE"


# City and country code (ZA = South Africa)
city = input("Enter city name: ") + ",ZA"

# OpenWeatherMap API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)
data = response.json()

# Print results
print("Weather in", city + ":")
print("Temperature:", data["main"]["temp"], "°C")
print("Feels like:", data["main"]["feels_like"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Condition:", data["weather"][0]["description"])
