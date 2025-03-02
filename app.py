from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API Key
API_KEY = 'your_openweathermap_api_key'

# Winter Facts
winter_facts = [
    "The coldest temperature ever recorded on Earth was −128.6°F (−89.2°C) in Antarctica.",
    "Winter is the best season to go skiing or snowboarding.",
    "Snowflakes come in many different shapes, but they are all six-sided!",
    "Polar bears' fur is not white, but transparent. It looks white because it reflects the snow.",
    "In many places, winter lasts for about three months from December to February."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    city = None
    country = None

    if request.method == 'POST':
        # Get the city and country from the form
        city = request.form.get('city')
        country = request.form.get('country')
        
        # Fetch weather data from OpenWeatherMap API
        if city and country:
            weather = get_weather(city, country)
        
    return render_template('index.html', weather=weather, winter_facts=winter_facts, city=city, country=country)

def get_weather(city, country):
    # Make API request to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant weather data
        main = data['main']
        weather_description = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']
        
        return {
            'temperature': temp,
            'description': weather_description,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)


