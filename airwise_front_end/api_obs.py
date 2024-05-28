#!/usr/bin/env python3

import requests
import json

def get_obstacle_data(bbox="40,-90,45,-85", format="json"):
    base_url = "http://www.aviationweather.gov/api/data/obstacle"
    params = {
        'bbox': bbox,
        'format': format
    }
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        if not response.content:
            print("Empty response")
            return None

        try:
            obstacle_data = response.json()
        except ValueError:
            print("Response is not valid JSON")
            return None

        if isinstance(obstacle_data, list):
            obstacles = []
            for data_point in obstacle_data:
                obstacle = {
                    "latitude": data_point.get("lat"),
                    "longitude": data_point.get("lon"),
                    "elevation": data_point.get("elev"),
                    "height": data_point.get("height"),
                    "type": data_point.get("type"),
                    "name": data_point.get("name")
                }
                obstacles.append(obstacle)
            return obstacles
        else:
            print("Unexpected response format")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

# Example usage
obstacle_data = get_obstacle_data(bbox="40,-90,45,-85", format="json")
if obstacle_data:
    # Convert the final output to JSON format and print it
    print(json.dumps(obstacle_data, indent=2))
