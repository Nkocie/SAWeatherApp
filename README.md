# SAWeatherApp 🌤️

A simple Python app to fetch real-time weather information for **any city in South Africa** using the **OpenWeatherMap API**.

---

## Features
- Get current temperature, humidity, and weather condition.
- Works for **any South African city**.
- Uses OpenWeatherMap API for accurate weather data.
- Easy to extend for other countries or coordinates.

---

## Requirements
- Python 3.x
- `requests` library

Install `requests` with:

```bash pip install requests ```

---

## Setup

1. Sign up for a free API key at OpenWeatherMap
2. Clone or download this repository to your local machine.
3. Open weather.py in a text editor.
4. Replace the placeholder API key: 'API_KEY = "YOUR_API_KEY_HERE"' with your actual API key.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder containing weather.py.
3. Run the script: 'python weather.py'

## Notes

-The app automatically appends ,ZA to ensure it fetches data for South African cities.
-If a city is not recognized, double-check the spelling or use geographic coordinates.
-Ensure your API key is valid and activated.
