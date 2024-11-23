#!/usr/bin/env python3
import requests
import json
import os
from datetime import datetime

def get_weather():
    try:
        # You'll need to get an API key from OpenWeatherMap
        API_KEY = 'API'
        # Set your city and country code
        CITY = 'Nha Trang'  # Change this to your city
        COUNTRY_CODE = 'VN'  # Change this to your country code
        
        # API endpoint
        url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric'
        
        # Get weather data
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = round(data['main']['temp'])
            description = data['weather'][0]['description']
            
            # Weather emoji mapping
            weather_emojis = {
                'clear sky': '☀️',
                'few clouds': '🌤️',
                'scattered clouds': '☁️',
                'broken clouds': '☁️',
                'shower rain': '🌧️',
                'rain': '🌧️',
                'thunderstorm': '⛈️',
                'snow': '🌨️',
                'mist': '🌫️'
            }
            
            emoji = weather_emojis.get(description, '🌡️')
            
            # Cache the result
            cache_dir = os.path.expanduser('~/.cache/fastfetch/')
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
                
            cache_file = os.path.join(cache_dir, 'weather_cache.json')
            cache_data = {
                'temperature': temp,
                'description': description,
                'emoji': emoji,
                'timestamp': datetime.now().timestamp()
            }
            
            with open(cache_file, 'w') as f:
                json.dump(cache_data, f)
            
            return f"{emoji} {temp}°C | {description}"
            
        else:
            # Try to read from cache if API call fails
            cache_file = os.path.expanduser('~/.cache/fastfetch/weather_cache.json')
            if os.path.exists(cache_file):
                with open(cache_file, 'r') as f:
                    cache_data = json.load(f)
                    return f"{cache_data['emoji']} {cache_data['temperature']}°C | {cache_data['description']}"
            return "Weather data unavailable"
            
    except Exception as e:
        # Try to read from cache if any error occurs
        try:
            cache_file = os.path.expanduser('~/.cache/fastfetch/weather_cache.json')
            if os.path.exists(cache_file):
                with open(cache_file, 'r') as f:
                    cache_data = json.load(f)
                    return f"{cache_data['emoji']} {cache_data['temperature']}°C | {cache_data['description']}"
        except:
            pass
        return "Weather data unavailable"

if __name__ == "__main__":
    print(get_weather())
