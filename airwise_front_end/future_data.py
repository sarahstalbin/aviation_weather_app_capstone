#!/usr/bin/env python3

import requests, json, os
from datetime import date, timedelta

def get_raw_weather_data(location='Seattle', current_state='future'):
    api_key = 'MZ9NPZ4W4R55YDEFCFQEVK3MV'
    city = location+',USA'


    if current_state == 'future':
        end_date = date.today()
        start_date=date.today() + timedelta(days=5)
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?key={api_key}'
    if current_state == 'past':
        end_date = date.today()
        start_date=date.today() - timedelta(days=5)
        url =f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?key={api_key}'



    headers = {'Accept': 'application/json'}
    try:
        # response = requests.get(base_url, headers = headers, params=params)
        # print("I am in try")
        response = requests.get(url, headers = headers)
        response.raise_for_status()  # Raise an error for bad status codes
        # print("I am after response")
        # Print the raw response content for debugging
        # print('Response content:', response.content)
        
        # If response content is empty or not valid JSON, handle it
        if not response.content:
            return 'Empty response'
        # weather_data = ""
        # Attempt to parse the JSON response
        try:
            weather_data = response.json()
            # if weather_data[0:3] == "HTTP":
            #     data_holder = {'queryCost': 6, 'latitude': 47.6036, 'longitude': -122.329, 'resolvedAddress': 'Seattle, WA, United States', 'address': 'Seatte,USA', 'timezone': 'America/Los_Angeles', 'tzoffset': -7.0, 'days': [{'datetime': '2024-05-27', 'datetimeEpoch': 1716793200, 'tempmax': 66.8, 'tempmin': 52.8, 'temp': 58.9, 'feelslikemax': 66.8, 'feelslikemin': 52.8, 'feelslike': 58.9, 'dew': 47.3, 'humidity': 66.3, 'precip': 0.0, 'precipprob': 0.0, 'precipcover': 0.0, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 9.2, 'windspeed': 9.6, 'winddir': 228.9, 'pressure': 1020.4, 'cloudcover': 72.8, 'visibility': 9.4, 'solarradiation': 210.9, 'solarenergy': 18.3, 'uvindex': 7.0, 'severerisk': 10.0, 'sunrise': '05:18:54', 'sunriseEpoch': 1716812334, 'sunset': '20:55:00', 'sunsetEpoch': 1716868500, 'moonphase': 0.65, 'conditions': 'Partially cloudy', 'description': 'Partly cloudy throughout the day.', 'icon': 'partly-cloudy-day', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-28', 'datetimeEpoch': 1716879600, 'tempmax': 60.3, 'tempmin': 51.6, 'temp': 55.0, 'feelslikemax': 60.3, 'feelslikemin': 51.6, 'feelslike': 55.0, 'dew': 46.8, 'humidity': 74.1, 'precip': 0.005, 'precipprob': 100.0, 'precipcover': 8.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 25.6, 'windspeed': 14.2, 'winddir': 188.1, 'pressure': 1019.6, 'cloudcover': 73.1, 'visibility': 9.4, 'solarradiation': 101.0, 'solarenergy': 8.7, 'uvindex': 4.0, 'severerisk': 10.0, 'sunrise': '05:18:07', 'sunriseEpoch': 1716898687, 'sunset': '20:56:01', 'sunsetEpoch': 1716954961, 'moonphase': 0.69, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with rain in the morning and afternoon.', 'icon': 'rain', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-29', 'datetimeEpoch': 1716966000, 'tempmax': 58.7, 'tempmin': 49.3, 'temp': 53.7, 'feelslikemax': 58.7, 'feelslikemin': 47.5, 'feelslike': 53.6, 'dew': 45.3, 'humidity': 73.5, 'precip': 0.101, 'precipprob': 100.0, 'precipcover': 33.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 21.0, 'windspeed': 14.0, 'winddir': 178.6, 'pressure': 1025.6, 'cloudcover': 87.3, 'visibility': 9.7, 'solarradiation': 124.2, 'solarenergy': 11.0, 'uvindex': 7.0, 'severerisk': 10.0, 'sunrise': '05:17:22', 'sunriseEpoch': 1716985042, 'sunset': '20:57:00', 'sunsetEpoch': 1717041420, 'moonphase': 0.72, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with rain.', 'icon': 'rain', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-30', 'datetimeEpoch': 1717052400, 'tempmax': 62.3, 'tempmin': 49.6, 'temp': 55.0, 'feelslikemax': 62.3, 'feelslikemin': 48.4, 'feelslike': 54.9, 'dew': 42.5, 'humidity': 64.7, 'precip': 0.005, 'precipprob': 100.0, 'precipcover': 8.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 19.7, 'windspeed': 8.8, 'winddir': 351.7, 'pressure': 1028.8, 'cloudcover': 73.1, 'visibility': 9.9, 'solarradiation': 278.5, 'solarenergy': 24.1, 'uvindex': 10.0, 'severerisk': 10.0, 'sunrise': '05:16:40', 'sunriseEpoch': 1717071400, 'sunset': '20:57:58', 'sunsetEpoch': 1717127878, 'moonphase': 0.75, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with early morning rain.', 'icon': 'rain', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-31', 'datetimeEpoch': 1717138800, 'tempmax': 71.0, 'tempmin': 46.5, 'temp': 58.9, 'feelslikemax': 71.0, 'feelslikemin': 46.5, 'feelslike': 58.9, 'dew': 42.4, 'humidity': 57.2, 'precip': 0.0, 'precipprob': 0.0, 'precipcover': 0.0, 'preciptype': None, 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 18.3, 'windspeed': 10.4, 'winddir': 321.3, 'pressure': 1021.0, 'cloudcover': 9.4, 'visibility': 9.9, 'solarradiation': 317.6, 'solarenergy': 27.4, 'uvindex': 9.0, 'severerisk': 10.0, 'sunrise': '05:16:00', 'sunriseEpoch': 1717157760, 'sunset': '20:58:55', 'sunsetEpoch': 1717214335, 'moonphase': 0.79, 'conditions': 'Clear', 'description': 'Clear conditions throughout the day.', 'icon': 'clear-day', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-01', 'datetimeEpoch': 1717225200, 'tempmax': 63.9, 'tempmin': 55.5, 'temp': 59.6, 'feelslikemax': 63.9, 'feelslikemin': 55.5, 'feelslike': 59.6, 'dew': 49.7, 'humidity': 70.4, 'precip': 0.06, 'precipprob': 40.0, 'precipcover': 20.83, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 12.8, 'windspeed': 8.1, 'winddir': 213.4, 'pressure': 1014.1, 'cloudcover': 69.6, 'visibility': 10.0, 'solarradiation': 142.0, 'solarenergy': 12.4, 'uvindex': 5.0, 'severerisk': 10.0, 'sunrise': '05:15:23', 'sunriseEpoch': 1717244123, 'sunset': '20:59:50', 'sunsetEpoch': 1717300790, 'moonphase': 0.83, 'conditions': 'Partially cloudy', 'description': 'Partly cloudy throughout the day.', 'icon': 'partly-cloudy-day', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'comb'}], 'stations': {'72793024233': {'distance': 17758.0, 'latitude': 47.444, 'longitude': -122.314, 'useCount': 0, 'id': '72793024233', 'name': 'SEATTLE TACOMA AIRPORT, WA US', 'quality': 100, 'contribution': 0.0}, 'KSEA': {'distance': 17237.0, 'latitude': 47.45, 'longitude': -122.3, 'useCount': 0, 'id': 'KSEA', 'name': 'KSEA', 'quality': 100, 'contribution': 0.0}, 'KBFI': {'distance': 8478.0, 'latitude': 47.53, 'longitude': -122.3, 'useCount': 0, 'id': 'KBFI', 'name': 'KBFI', 'quality': 100, 'contribution': 0.0}, '72793524234': {'distance': 8426.0, 'latitude': 47.53, 'longitude': -122.301, 'useCount': 0, 'id': '72793524234', 'name': 'SEATTLE BOEING FIELD, WA US', 'quality': 100, 'contribution': 0.0}, '72793494248': {'distance': 15014.0, 'latitude': 47.493, 'longitude': -122.214, 'useCount': 0, 'id': '72793494248', 'name': 'RENTON MUNICIPAL AIRPORT, WA US', 'quality': 100, 'contribution': 0.0}, 'F0821': {'distance': 1449.0, 'latitude': 47.612, 'longitude': -122.314, 'useCount': 0, 'id': 'F0821', 'name': 'FW0821 Seattle WA US', 'quality': 0, 'contribution': 0.0}, 'KRNT': {'distance': 14145.0, 'latitude': 47.5, 'longitude': -122.22, 'useCount': 0, 'id': 'KRNT', 'name': 'KRNT', 'quality': 100, 'contribution': 0.0}}}
            # print('this is weather data', weather_data)
            return weather_data
           
            
            
            # print('\n')
        except ValueError:
            print('Response is not valid JSON')
            return None
            
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        if current_state == 'past':
            data_holder = {'queryCost': 6, 'latitude': 47.6036, 'longitude': -122.329, 'resolvedAddress': 'Seattle, WA, United States', 'address': 'Seatte,USA', 'timezone': 'America/Los_Angeles', 'tzoffset': -7.0, 'days': [{'datetime': '2024-05-27', 'datetimeEpoch': 1716793200, 'tempmax': 66.8, 'tempmin': 52.8, 'temp': 58.9, 'feelslikemax': 66.8, 'feelslikemin': 52.8, 'feelslike': 58.9, 'dew': 47.3, 'humidity': 66.3, 'precip': 0.0, 'precipprob': 0.0, 'precipcover': 0.0, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 9.2, 'windspeed': 9.6, 'winddir': 228.9, 'pressure': 1020.4, 'cloudcover': 72.8, 'visibility': 9.4, 'solarradiation': 210.9, 'solarenergy': 18.3, 'uvindex': 7.0, 'severerisk': 10.0, 'sunrise': '05:18:54', 'sunriseEpoch': 1716812334, 'sunset': '20:55:00', 'sunsetEpoch': 1716868500, 'moonphase': 0.65, 'conditions': 'Partially cloudy', 'description': 'Partly cloudy throughout the day.', 'icon': 'partly-cloudy-day', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-28', 'datetimeEpoch': 1716879600, 'tempmax': 60.3, 'tempmin': 51.6, 'temp': 55.0, 'feelslikemax': 60.3, 'feelslikemin': 51.6, 'feelslike': 55.0, 'dew': 46.8, 'humidity': 74.1, 'precip': 0.005, 'precipprob': 100.0, 'precipcover': 8.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 25.6, 'windspeed': 14.2, 'winddir': 188.1, 'pressure': 1019.6, 'cloudcover': 73.1, 'visibility': 9.4, 'solarradiation': 101.0, 'solarenergy': 8.7, 'uvindex': 4.0, 'severerisk': 10.0, 'sunrise': '05:18:07', 'sunriseEpoch': 1716898687, 'sunset': '20:56:01', 'sunsetEpoch': 1716954961, 'moonphase': 0.69, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with rain in the morning and afternoon.', 'icon': 'rain', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-29', 'datetimeEpoch': 1716966000, 'tempmax': 58.7, 'tempmin': 49.3, 'temp': 53.7, 'feelslikemax': 58.7, 'feelslikemin': 47.5, 'feelslike': 53.6, 'dew': 45.3, 'humidity': 73.5, 'precip': 0.101, 'precipprob': 100.0, 'precipcover': 33.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 21.0, 'windspeed': 14.0, 'winddir': 178.6, 'pressure': 1025.6, 'cloudcover': 87.3, 'visibility': 9.7, 'solarradiation': 124.2, 'solarenergy': 11.0, 'uvindex': 7.0, 'severerisk': 10.0, 'sunrise': '05:17:22', 'sunriseEpoch': 1716985042, 'sunset': '20:57:00', 'sunsetEpoch': 1717041420, 'moonphase': 0.72, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with rain.', 'icon': 'rain', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-30', 'datetimeEpoch': 1717052400, 'tempmax': 62.3, 'tempmin': 49.6, 'temp': 55.0, 'feelslikemax': 62.3, 'feelslikemin': 48.4, 'feelslike': 54.9, 'dew': 42.5, 'humidity': 64.7, 'precip': 0.005, 'precipprob': 100.0, 'precipcover': 8.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 19.7, 'windspeed': 8.8, 'winddir': 351.7, 'pressure': 1028.8, 'cloudcover': 73.1, 'visibility': 9.9, 'solarradiation': 278.5, 'solarenergy': 24.1, 'uvindex': 10.0, 'severerisk': 10.0, 'sunrise': '05:16:40', 'sunriseEpoch': 1717071400, 'sunset': '20:57:58', 'sunsetEpoch': 1717127878, 'moonphase': 0.75, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with early morning rain.', 'icon': 'rain', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-05-31', 'datetimeEpoch': 1717138800, 'tempmax': 71.0, 'tempmin': 46.5, 'temp': 58.9, 'feelslikemax': 71.0, 'feelslikemin': 46.5, 'feelslike': 58.9, 'dew': 42.4, 'humidity': 57.2, 'precip': 0.0, 'precipprob': 0.0, 'precipcover': 0.0, 'preciptype': None, 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 18.3, 'windspeed': 10.4, 'winddir': 321.3, 'pressure': 1021.0, 'cloudcover': 9.4, 'visibility': 9.9, 'solarradiation': 317.6, 'solarenergy': 27.4, 'uvindex': 9.0, 'severerisk': 10.0, 'sunrise': '05:16:00', 'sunriseEpoch': 1717157760, 'sunset': '20:58:55', 'sunsetEpoch': 1717214335, 'moonphase': 0.79, 'conditions': 'Clear', 'description': 'Clear conditions throughout the day.', 'icon': 'clear-day', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-01', 'datetimeEpoch': 1717225200, 'tempmax': 63.9, 'tempmin': 55.5, 'temp': 59.6, 'feelslikemax': 63.9, 'feelslikemin': 55.5, 'feelslike': 59.6, 'dew': 49.7, 'humidity': 70.4, 'precip': 0.06, 'precipprob': 40.0, 'precipcover': 20.83, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 12.8, 'windspeed': 8.1, 'winddir': 213.4, 'pressure': 1014.1, 'cloudcover': 69.6, 'visibility': 10.0, 'solarradiation': 142.0, 'solarenergy': 12.4, 'uvindex': 5.0, 'severerisk': 10.0, 'sunrise': '05:15:23', 'sunriseEpoch': 1717244123, 'sunset': '20:59:50', 'sunsetEpoch': 1717300790, 'moonphase': 0.83, 'conditions': 'Partially cloudy', 'description': 'Partly cloudy throughout the day.', 'icon': 'partly-cloudy-day', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'comb'}], 'stations': {'72793024233': {'distance': 17758.0, 'latitude': 47.444, 'longitude': -122.314, 'useCount': 0, 'id': '72793024233', 'name': 'SEATTLE TACOMA AIRPORT, WA US', 'quality': 100, 'contribution': 0.0}, 'KSEA': {'distance': 17237.0, 'latitude': 47.45, 'longitude': -122.3, 'useCount': 0, 'id': 'KSEA', 'name': 'KSEA', 'quality': 100, 'contribution': 0.0}, 'KBFI': {'distance': 8478.0, 'latitude': 47.53, 'longitude': -122.3, 'useCount': 0, 'id': 'KBFI', 'name': 'KBFI', 'quality': 100, 'contribution': 0.0}, '72793524234': {'distance': 8426.0, 'latitude': 47.53, 'longitude': -122.301, 'useCount': 0, 'id': '72793524234', 'name': 'SEATTLE BOEING FIELD, WA US', 'quality': 100, 'contribution': 0.0}, '72793494248': {'distance': 15014.0, 'latitude': 47.493, 'longitude': -122.214, 'useCount': 0, 'id': '72793494248', 'name': 'RENTON MUNICIPAL AIRPORT, WA US', 'quality': 100, 'contribution': 0.0}, 'F0821': {'distance': 1449.0, 'latitude': 47.612, 'longitude': -122.314, 'useCount': 0, 'id': 'F0821', 'name': 'FW0821 Seattle WA US', 'quality': 0, 'contribution': 0.0}, 'KRNT': {'distance': 14145.0, 'latitude': 47.5, 'longitude': -122.22, 'useCount': 0, 'id': 'KRNT', 'name': 'KRNT', 'quality': 100, 'contribution': 0.0}}}
            return data_holder
        if current_state == 'future':
            data_holder = {'queryCost': 6, 'latitude': 47.6036, 'longitude': -122.329, 'resolvedAddress': 'Seattle, WA, United States', 'address': 'Seatte,USA', 'timezone': 'America/Los_Angeles', 'tzoffset': -7.0, 'days': [{'datetime': '2024-06-1', 'datetimeEpoch': 1716793200, 'tempmax': 66.8, 'tempmin': 52.8, 'temp': 58.9, 'feelslikemax': 66.8, 'feelslikemin': 52.8, 'feelslike': 58.9, 'dew': 47.3, 'humidity': 66.3, 'precip': 0.0, 'precipprob': 0.0, 'precipcover': 0.0, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 9.2, 'windspeed': 9.6, 'winddir': 228.9, 'pressure': 1020.4, 'cloudcover': 72.8, 'visibility': 9.4, 'solarradiation': 210.9, 'solarenergy': 18.3, 'uvindex': 7.0, 'severerisk': 10.0, 'sunrise': '05:18:54', 'sunriseEpoch': 1716812334, 'sunset': '20:55:00', 'sunsetEpoch': 1716868500, 'moonphase': 0.65, 'conditions': 'Partially cloudy', 'description': 'Partly cloudy throughout the day.', 'icon': 'partly-cloudy-day', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-2', 'datetimeEpoch': 1716879600, 'tempmax': 60.3, 'tempmin': 51.6, 'temp': 55.0, 'feelslikemax': 60.3, 'feelslikemin': 51.6, 'feelslike': 55.0, 'dew': 46.8, 'humidity': 74.1, 'precip': 0.005, 'precipprob': 100.0, 'precipcover': 8.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 25.6, 'windspeed': 14.2, 'winddir': 188.1, 'pressure': 1019.6, 'cloudcover': 73.1, 'visibility': 9.4, 'solarradiation': 101.0, 'solarenergy': 8.7, 'uvindex': 4.0, 'severerisk': 10.0, 'sunrise': '05:18:07', 'sunriseEpoch': 1716898687, 'sunset': '20:56:01', 'sunsetEpoch': 1716954961, 'moonphase': 0.69, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with rain in the morning and afternoon.', 'icon': 'rain', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-3', 'datetimeEpoch': 1716966000, 'tempmax': 58.7, 'tempmin': 49.3, 'temp': 53.7, 'feelslikemax': 58.7, 'feelslikemin': 47.5, 'feelslike': 53.6, 'dew': 45.3, 'humidity': 73.5, 'precip': 0.101, 'precipprob': 100.0, 'precipcover': 33.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 21.0, 'windspeed': 14.0, 'winddir': 178.6, 'pressure': 1025.6, 'cloudcover': 87.3, 'visibility': 9.7, 'solarradiation': 124.2, 'solarenergy': 11.0, 'uvindex': 7.0, 'severerisk': 10.0, 'sunrise': '05:17:22', 'sunriseEpoch': 1716985042, 'sunset': '20:57:00', 'sunsetEpoch': 1717041420, 'moonphase': 0.72, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with rain.', 'icon': 'rain', 'stations': ['72793024233', 'KSEA', 'KBFI', '72793524234', '72793494248', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-4', 'datetimeEpoch': 1717052400, 'tempmax': 62.3, 'tempmin': 49.6, 'temp': 55.0, 'feelslikemax': 62.3, 'feelslikemin': 48.4, 'feelslike': 54.9, 'dew': 42.5, 'humidity': 64.7, 'precip': 0.005, 'precipprob': 100.0, 'precipcover': 8.33, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 19.7, 'windspeed': 8.8, 'winddir': 351.7, 'pressure': 1028.8, 'cloudcover': 73.1, 'visibility': 9.9, 'solarradiation': 278.5, 'solarenergy': 24.1, 'uvindex': 10.0, 'severerisk': 10.0, 'sunrise': '05:16:40', 'sunriseEpoch': 1717071400, 'sunset': '20:57:58', 'sunsetEpoch': 1717127878, 'moonphase': 0.75, 'conditions': 'Rain, Partially cloudy', 'description': 'Partly cloudy throughout the day with early morning rain.', 'icon': 'rain', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-5', 'datetimeEpoch': 1717138800, 'tempmax': 71.0, 'tempmin': 46.5, 'temp': 58.9, 'feelslikemax': 71.0, 'feelslikemin': 46.5, 'feelslike': 58.9, 'dew': 42.4, 'humidity': 57.2, 'precip': 0.0, 'precipprob': 0.0, 'precipcover': 0.0, 'preciptype': None, 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 18.3, 'windspeed': 10.4, 'winddir': 321.3, 'pressure': 1021.0, 'cloudcover': 9.4, 'visibility': 9.9, 'solarradiation': 317.6, 'solarenergy': 27.4, 'uvindex': 9.0, 'severerisk': 10.0, 'sunrise': '05:16:00', 'sunriseEpoch': 1717157760, 'sunset': '20:58:55', 'sunsetEpoch': 1717214335, 'moonphase': 0.79, 'conditions': 'Clear', 'description': 'Clear conditions throughout the day.', 'icon': 'clear-day', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'obs'}, {'datetime': '2024-06-06', 'datetimeEpoch': 1717225200, 'tempmax': 63.9, 'tempmin': 55.5, 'temp': 59.6, 'feelslikemax': 63.9, 'feelslikemin': 55.5, 'feelslike': 59.6, 'dew': 49.7, 'humidity': 70.4, 'precip': 0.06, 'precipprob': 40.0, 'precipcover': 20.83, 'preciptype': ['rain'], 'snow': 0.0, 'snowdepth': 0.0, 'windgust': 12.8, 'windspeed': 8.1, 'winddir': 213.4, 'pressure': 1014.1, 'cloudcover': 69.6, 'visibility': 10.0, 'solarradiation': 142.0, 'solarenergy': 12.4, 'uvindex': 5.0, 'severerisk': 10.0, 'sunrise': '05:15:23', 'sunriseEpoch': 1717244123, 'sunset': '20:59:50', 'sunsetEpoch': 1717300790, 'moonphase': 0.83, 'conditions': 'Partially cloudy', 'description': 'Partly cloudy throughout the day.', 'icon': 'partly-cloudy-day', 'stations': ['KSEA', 'KBFI', 'F0821', 'KRNT'], 'source': 'comb'}], 'stations': {'72793024233': {'distance': 17758.0, 'latitude': 47.444, 'longitude': -122.314, 'useCount': 0, 'id': '72793024233', 'name': 'SEATTLE TACOMA AIRPORT, WA US', 'quality': 100, 'contribution': 0.0}, 'KSEA': {'distance': 17237.0, 'latitude': 47.45, 'longitude': -122.3, 'useCount': 0, 'id': 'KSEA', 'name': 'KSEA', 'quality': 100, 'contribution': 0.0}, 'KBFI': {'distance': 8478.0, 'latitude': 47.53, 'longitude': -122.3, 'useCount': 0, 'id': 'KBFI', 'name': 'KBFI', 'quality': 100, 'contribution': 0.0}, '72793524234': {'distance': 8426.0, 'latitude': 47.53, 'longitude': -122.301, 'useCount': 0, 'id': '72793524234', 'name': 'SEATTLE BOEING FIELD, WA US', 'quality': 100, 'contribution': 0.0}, '72793494248': {'distance': 15014.0, 'latitude': 47.493, 'longitude': -122.214, 'useCount': 0, 'id': '72793494248', 'name': 'RENTON MUNICIPAL AIRPORT, WA US', 'quality': 100, 'contribution': 0.0}, 'F0821': {'distance': 1449.0, 'latitude': 47.612, 'longitude': -122.314, 'useCount': 0, 'id': 'F0821', 'name': 'FW0821 Seattle WA US', 'quality': 0, 'contribution': 0.0}, 'KRNT': {'distance': 14145.0, 'latitude': 47.5, 'longitude': -122.22, 'useCount': 0, 'id': 'KRNT', 'name': 'KRNT', 'quality': 100, 'contribution': 0.0}}}
            return data_holder
        # print('this is weather data', data_holder)
        return http_err
    #    except requests.exceptions.RequestException as req_err:
    #       print(f'Request error occurred: {req_err}')
    #  except ET.ParseError as parse_err:
    #     print(f'XML parse error: {parse_err}')
    #print("this is weather data in get_hist_data",weather_data)
    


def filter_weather_data(location='Seattle',current_state='future'):
    weather_data = get_raw_weather_data(location, current_state)
    # print(f"This is weather data in filter weather {weather_data}")
    if weather_data is None:
        return ""
    print(f"This is weather data in get weather {weather_data}")
    wind_temp_data = []
    for site in weather_data['days']:
        value = {
            'datetime': site['datetime'],
            'tempmax': site['tempmax'],
            'tempmin': site['tempmin'],
            'temp': site['temp'],
            'dew': site['dew'],
            'humidity': site['humidity'],
            'precip': site['precip'],
            'snow': site['snow'],

            'windgust': site['windgust'],
            'winddir': site['winddir'],
            'pressure': site['pressure'],
            'cloudcover': site['cloudcover'],
            'visibility': site['visibility'],
            
            'solarradiation': site['solarradiation'],
            'solarenergy': site['solarenergy'],
            'uvindex': site['uvindex'],
            'severerisk': site['severerisk'],
            'sunrise': site['sunrise'],

            'sunriseEpoch': site['sunriseEpoch'],
            'sunset': site['sunset'],
            'sunsetEpoch': site['sunsetEpoch'],
            'moonphase': site['moonphase'],
            'conditions': site['conditions'],
        }
        wind_temp_data.append(value)
        # print(f"this is after dictionary {value}")
        # print('\n')
    # print("I am wind temp",wind_temp_data)

    return wind_temp_data



def get_daily_data(location='Seattle'):
    forecast_information = get_raw_weather_data(location, current_state='future')
    if not forecast_information:
        return 'No data for selected parameters'
    forecast_dict = []
    # print(f"This is forecast information {forecast_information}")
    for site in forecast_information:
        if site != 'days':
            value = {
                site: forecast_information.get(site)
            }
            forecast_dict.append(value)
        # print(value)
        # print(f"this is forecast after dictionary {forecast_dict}")
        # print('\n')

    return forecast_dict


def get_past_data(location='Seattle',type='temp', past=True):
    past = True
    forecast_data = get_weather_data(location, past)
    # type = str(type)
    if type[0] == "'":
        type = type[1:-1]
    weather_dict=[]
    if not forecast_data:
        # print(type)
        # print(location)
        return 'No data for selected parameters'

    for data in forecast_data:
        # if type in hist_data:
        single_day = {
            'datetime': data['datetime'],
            type: data[type]
         }
        weather_dict.append(single_day)

    return weather_dict

def specific_data(location='Seattle',type='temp', current_state='future'):
    
    if current_state[0] == "'":
        current_state = current_state[1:-1]
    forecast_data = filter_weather_data(location, current_state)
    if type[0] == "'":
        type = type[1:-1]
    weather_dict=[]
    if not forecast_data:
        holder = {
            'datetime': '2024-6-1',
            type: 5
        }
        weather_dict.append(holder)
        print('No data for selected parameters')

    for data in forecast_data:
        # if type in hist_data:
        single_day = {
            'datetime': data['datetime'],
            type: data[type]
         }
        weather_dict.append(single_day)

    return weather_dict



if __name__ == '__main__':
    
    print(specific_data('Seatte','temp', 'past'))
