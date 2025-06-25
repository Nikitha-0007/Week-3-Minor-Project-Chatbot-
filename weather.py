import requests 

API_KEY = "YourAPIKey"
CITY = "Hyderabad"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"🌤️ Weather in {CITY}: {temp}°C, {desc}"
    except:
        return "Failed to fetch weather data."
