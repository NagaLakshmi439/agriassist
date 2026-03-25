import requests

# 🔑 Replace this with your own API key
API_KEY = "your_api_key_here"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("main"):
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            return f"🌤 Weather in {city}: {description}, Temp: {temperature}°C, Humidity: {humidity}%"
        else:
            return "❌ City not found"

    except:
        return "❌ Error fetching weather data"
