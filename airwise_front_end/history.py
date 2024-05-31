#!/usr/bin/env python3

import requests, json

def get_hist_data():
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK?key=EBBMX4R5X9X9EYAYQ4S9FNDS4" 
    
    # params = {
    #     'queryCost': 1,
    #     'address': 'London,UK',
    #     'timezone': 'Europe/London',
    #     'tzoffset' : 1.0
    # }
    headers = {"Accept": "application/json"}
    try:
        # response = requests.get(base_url, headers = headers, params=params)
        response = requests.get(url, headers = headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Print the raw response content for debugging
        # print("Response content:", response.content)
        
        # If response content is empty or not valid JSON, handle it
        if not response.content:
            print("Empty response")
            return None

        # Attempt to parse the JSON response
        try:
            weather_data = response.json()
            # print(weather_data)
            # print('\n')
        except ValueError:
            print("Response is not valid JSON")
            return None

        # value = weather_data.get('id')
        # value = weather_data['icaoID']
        # print("value",value)
        input_id = "LSMM"
        wind_temp_data = []
        for site in weather_data['days']:
            value = {
                "datetime": site['datetime'],
                "tempmax": site['tempmax'],
                "tempmin": site['tempmin'],
                "temp": site['temp'],
                "dew": site['dew'],
                "humidity": site['humidity'],
                "precip": site['precip'],
                "snow": site['snow'],

                "windgust": site['windgust'],
                "winddir": site['winddir'],
                "pressure": site['pressure'],
                "cloudcover": site['cloudcover'],
                "visibility": site['visibility'],
                
                "solarradiation": site['solarradiation'],
                "solarenergy": site['solarenergy'],
                "uvindex": site['uvindex'],
                "severerisk": site['severerisk'],
                "sunrise": site['sunrise'],

                "sunriseEpoch": site['sunriseEpoch'],
                "sunset": site['sunset'],
                "sunsetEpoch": site['sunsetEpoch'],
                "moonphase": site['moonphase'],
                "conditions": site['conditions'],
            }
            wind_temp_data.append(value)
            # print(value)
            # print('\n')

        return wind_temp_data
    
        # Process the weather data as needed
        # print("Weather data:", weather_data)
        if 'data' not in weather_data:
            print("No data found in response")
            return None
                
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
#    except requests.exceptions.RequestException as req_err:
#       print(f"Request error occurred: {req_err}")
#  except ET.ParseError as parse_err:
#     print(f"XML parse error: {parse_err}")
    return None


def specific_data():

    hist_data = get_hist_data()
    # print(f"this is hist_data: {hist_data}")
    weather_dict=[]
    for data in hist_data:
        # print(data['datetime'])
        single_day = {
            "datetime": data['datetime'],
            "temp": data['temp'],
            "humidity": data['humidity'],
            "precip": data['precip'],
        }

        weather_dict.append(single_day)

    return weather_dict
        # if data['datetime'] =='2024-05-27':
        #     print(data['tempmax'])
        # "datetime": data['datetime'],
        # "tempmax": data['tempmax'],
            # "tempmin": site['tempmin'],
            # "temp": site['temp'],
            # "dew": site['dew'],

            # "snow": site['snow'],

            # "windgust": site['windgust'],
            # "winddir": site['winddir'],
            # "pressure": site['pressure'],
            # "cloudcover": site['cloudcover'],
            # "visibility": site['visibility'],
            
            # "solarradiation": site['solarradiation'],
            # "solarenergy": site['solarenergy'],
            # "uvindex": site['uvindex'], 
            # "severerisk": site['severerisk'],
            # "sunrise": site['sunrise'],

            # "sunriseEpoch": site['sunriseEpoch'],
            # "sunset": site['sunset'],
            # "sunsetEpoch": site['sunsetEpoch'],
            # "moonphase": site['moonphase'],
            # "conditions": site['conditions']


if __name__ == '__main__':
    output = specific_data()
    # print(output)
