#!/usr/bin/env python3

import requests
#import xml.etree.ElementTree as ET

def get_wind_temp_data(region="other_pac", level="low", fcst="12"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
#    base_url = "https://www.aviationweather.gov/windtemp/data"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
    }
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Print the raw response content for debugging
        print("Response content:", response.content)
        
        # If response content is empty or not valid JSON, handle it
        if not response.content:
            print("Empty response")
            return None

        # Attempt to parse the JSON response
        try:
            weather_data = response.json()
        except ValueError:
            print("Response is not valid JSON")
            return None

        # Process the weather data as needed
        wind_temp_data = []
        for data_point in weather_data.get('data', []):
            wind_temp = {
                "latitude": data_point.get("latitude"),
                "longitude": data_point.get("longitude"),
                "wind_speed": data_point.get("wind_speed"),
                "wind_direction": data_point.get("wind_direction"),
                "temperature": data_point.get("temperature")
            }
            wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
#    except requests.exceptions.RequestException as req_err:
 #       print(f"Request error occurred: {req_err}")
  #  except ET.ParseError as parse_err:
   #     print(f"XML parse error: {parse_err}")
    return None

# Example usage
wind_temp_data = get_wind_temp_data(region="other_pac", level="low", fcst="12")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    for data in wind_temp_data:
        print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}, "
              f"Wind Speed: {data['wind_speed']} kt, Wind Direction: {data['wind_direction']} degrees, "
              f"Temperature: {data['temperature']} C")
