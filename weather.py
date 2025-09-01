import requests

# Your API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY_HERE"

# City and country code (ZA = South Africa)
city = input("Enter city name: ")+",ZA"

# Coordinates for Hlabisa (fallback)
# latitude = -28.2103
# longitude = 31.9947

# First, try with city name
url_city = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url_city)
data = response.json()

# If city not found, try with latitude/longitude
if response.status_code != 200 or "main" not in data:
    print(f"City '{city}' not found. Enter coordinates instead...")
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    url_coords = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url_coords)
    data = response.json()

# Now check again and print results
if response.status_code == 200 and "main" in data:
    print("Weather in Hlabisa, ZA:")
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])
else:
    print("Error:", data.get("message", "Unable to fetch weather data"))
