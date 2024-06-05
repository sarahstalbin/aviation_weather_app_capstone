#!/usr/bin/env python3

import requests

def seatac():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=47.443546&lon=-122.301659&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
    response = requests.get(url)
    weather_data = response.json()  # Parse the JSON response
    wind_temp_data = []
    temperature = int(round((weather_data['main']['temp'] - 273.15) * (9/5) + 32))
    feels_like_temp = int(round((weather_data['main']['feels_like'] - 273.15) * (9/5) + 32))

    # Create the wind_temp dictionary with the relevant data
    wind_temp = {
 #       "id": weather_data['id'],
        "name" : weather_data['name'],
        "country": weather_data['sys']['country'],
        "id": weather_data['id'],
        "lat": weather_data['coord']['lat'],
        "lon": weather_data['coord']['lon'],
        "deg": weather_data['wind']['deg'],
        "speed": weather_data['wind']['speed'],
        "temp": temperature,
        "feels_like": feels_like_temp,
        "pressure": weather_data['main']['pressure'],
        "humidity": weather_data['main']['humidity'],
        "visibility": weather_data['visibility'],
        "weather_desc": []
    }
    for items in weather_data['weather']:
        wind_temp['weather_desc'] = items['icon']
    wind_temp_data.append(wind_temp)

    print(wind_temp_data)
    return wind_temp_data

# seatac()

def white_center():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=47.52997&lon=-122.30194&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
   # url = "https://api.openweathermap.org/data/2.5/weather?lat=47.90732&lon=-122.28209,&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
    response = requests.get(url)
    weather_data = response.json()  # Parse the JSON response

    wind_temp_data = []
    temperature = int(round((weather_data['main']['temp'] - 273.15) * (9/5) + 32))
    feels_like_temp = int(round((weather_data['main']['feels_like'] - 273.15) * (9/5) + 32))

    # Create the wind_temp dictionary with the relevant data
    wind_temp = {
        "id": weather_data['id'],
        "name" : weather_data['name'],
        "country": weather_data['sys']['country'],
        "id": weather_data['id'],
        "lat": weather_data['coord']['lat'],
        "lon": weather_data['coord']['lon'],
        "deg": weather_data['wind']['deg'],
        "speed": weather_data['wind']['speed'],
        "temp": temperature,
        "feels_like": feels_like_temp,
        "pressure": weather_data['main']['pressure'],
        "humidity": weather_data['main']['humidity'],
        "visibility": weather_data['visibility'],
        "weather_desc": []
    }
    for items in weather_data['weather']:
        wind_temp['weather_desc'] = items['icon']
    wind_temp_data.append(wind_temp)

    wind_temp_data.append(wind_temp)

    print(wind_temp_data)
    return wind_temp_data

#    print(response.text)
# white_center()
def spokane():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=47.61903&lon=-117.53522&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
   # url = "https://api.openweathermap.org/data/2.5/weather?lat=47.90732&lon=-122.28209,&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
    response = requests.get(url)
    weather_data = response.json()  # Parse the JSON response

    wind_temp_data = []
    temperature = int(round((weather_data['main']['temp'] - 273.15) * (9/5) + 32))
    feels_like_temp = int(round((weather_data['main']['feels_like'] - 273.15) * (9/5) + 32))

    # Create the wind_temp dictionary with the relevant data
    wind_temp = {
        "id": weather_data['id'],
        "name" : weather_data['name'],
        "country": weather_data['sys']['country'],
        "id": weather_data['id'],
        "lat": weather_data['coord']['lat'],
        "lon": weather_data['coord']['lon'],
        "deg": weather_data['wind']['deg'],
        "speed": weather_data['wind']['speed'],
        "temp": temperature,
        "feels_like": feels_like_temp,
        "pressure": weather_data['main']['pressure'],
        "humidity": weather_data['main']['humidity'],
        "visibility": weather_data['visibility'],
        "weather_desc": []
    }
    for items in weather_data['weather']:
        wind_temp['weather_desc'] = items['icon']
    wind_temp_data.append(wind_temp)

    print(wind_temp_data)
    return wind_temp_data

#    print(response.text)
# spokane()


def pullman():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=46.74169&lon=-117.11162&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
   # url = "https://api.openweathermap.org/data/2.5/weather?lat=47.90732&lon=-122.28209,&appid=0827de6f708a7f3fc42e0ea4290eb9c9"
    response = requests.get(url)
    weather_data = response.json()  # Parse the JSON response
    # print(weather_data)

    wind_temp_data = []
    temperature = int(round((weather_data['main']['temp'] - 273.15) * (9/5) + 32))
    feels_like_temp = int(round((weather_data['main']['feels_like'] - 273.15) * (9/5) + 32))

    # Create the wind_temp dictionary with the relevant data
    wind_temp = {
        "id": weather_data['id'],
        "name" : weather_data['name'],
        "country": weather_data['sys']['country'],
        "id": weather_data['id'],
        "lat": weather_data['coord']['lat'],
        "lon": weather_data['coord']['lon'],
        "deg": weather_data['wind']['deg'],
        "speed": weather_data['wind']['speed'],
        "temp": temperature,
        "feels_like": feels_like_temp,
        "pressure": weather_data['main']['pressure'],
        "humidity": weather_data['main']['humidity'],
        "visibility": weather_data['visibility'],
        "weather_desc": []
    }
    for items in weather_data['weather']:
        wind_temp['weather_desc'] = items['icon']
    wind_temp_data.append(wind_temp)

    # print(wind_temp_data)
    return wind_temp_data

# pullman()
