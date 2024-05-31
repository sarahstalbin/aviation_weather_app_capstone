import requests
import json
url = "https://api.tomorrow.io/v4/weather/forecast?location=42.3478%2C-71.0466&apikey=1Z227T74khoF5NIhhf5B8z5YPlOQtARv"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
#obstacle_data = get_obstacle_data(bbox="40,-90,45,-85", format="json")
#if obstacle_data:
    # Convert the final output to JSON format and print it
#print(json.dumps(response.text, indent=2))


print(response.text)
