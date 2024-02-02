import requests

api_key = "a7e1657d6c4b3e12d0d58f5eec82d436"
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather(data):
    if data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
    else:
        print("No weather data to display.")
        
location = input("Enter the city or ZIP code: ")
weather_data = get_weather(api_key, location)
if weather_data:
    display_weather(weather_data)




    
