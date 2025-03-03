import requests

# OpenWeatherMap API Key
API_KEY = '9051261a9584b0760f796d0c04f55a6f'  # Replace with your actual API key

# Function to fetch weather data
def get_weather(city, country):
    # Construct the URL to call the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"
    
    # Make the request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Parse the response to JSON
        
        # Extract relevant data from the response
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        # Return weather details
        return {
            'temperature': main['temp'],
            'description': weather['description'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed']
        }
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
city = input("Enter city: ")
country = input("Enter country: ")

weather = get_weather(city, country)

if weather:
    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
else:
    print("Could not fetch weather data.")



