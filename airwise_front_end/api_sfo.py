#!/usr/bin/env python3

import requests


def get_sfo(region="sfo", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                }
                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None

def get_hawaii(region="hawaii", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                }
                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_all(region="all", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                }
                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_alaska(region="alaska", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                 }
                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_other_pac(region="other_pac", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                }
                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_south_central(region="dfw", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                }

                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_north_central(region="chi", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                 }

                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_rocky_mountain(region="slc", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                 }

                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_north_east(region="bos", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                 }

                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
def get_south_east(region="mia", level="low", fcst="06"):
    base_url = "http://www.aviationweather.gov/api/data/windtemp"
    params = {
        'region': region,
        'level': level,
        'fcst': fcst
     }

    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers = headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

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
        wind_temp_data = []
        for site in weather_data['sites']:
                wind_temp = {
                    "id": site['id'],
                    "lat": site['lat'],
                    "lon": site['lon'],
                    "dir": site['dir'],
                    "spd": site['spd'],
                 }

                wind_temp_data.append(wind_temp)
        return wind_temp_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None

# Example usage
wind_temp_data = get_sfo(region="sfo", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)

# Example usage
wind_temp_data = get_hawaii(region="hawaii", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)

# Example usage
wind_temp_data = get_all(region="all", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)
# Example usage
wind_temp_data = get_alaska(region="alaska", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)
# Example usage
wind_temp_data = get_other_pac(region="other_pac", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)

# Example usage
wind_temp_data = get_rocky_mountain(region="slc", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)

# Example usage
wind_temp_data = get_south_central(region="dfw", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)

# Example usage
wind_temp_data = get_north_central(region="chi", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)
# Example usage
wind_temp_data = get_north_east(region="bos", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)
# Example usage
wind_temp_data = get_south_east(region="mia", level="low", fcst="06")  # Fetch wind and temperature data for SFO region
if wind_temp_data:
    print(wind_temp_data)
