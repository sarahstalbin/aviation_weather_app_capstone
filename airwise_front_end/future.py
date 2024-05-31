#!/usr/bin/env python3

import requests, json, os

def get_hist_data(location='Seattle'):
   
    api_key = 'EBBMX4R5X9X9EYAYQ4S9FNDS4'
    city = location+',USA'
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={api_key}' 
    # url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?locations={location}&aggregateHours=24&unitGroup=us&shortColumnNames=false&contentType=csv&key={api_key}'


    
    # params = {
    #     'queryCost': 1,
        # 'address': 'London,UK',
    #     'timezone': 'Europe/London',
    #     'tzoffset' : 1.0
    # }
    headers = {'Accept': 'application/json'}
    try:
        # response = requests.get(base_url, headers = headers, params=params)
        response = requests.get(url, headers = headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Print the raw response content for debugging
        # print('Response content:', response.content)
        
        # If response content is empty or not valid JSON, handle it
        if not response.content:
            print('Empty response')
            return None

        # Attempt to parse the JSON response
        try:
            weather_data = response.json()
            # print(weather_data)
            # print('\n')
        except ValueError:
            print('Response is not valid JSON')
            return None

        # value = weather_data.get('id')
        # value = weather_data['icaoID']
        # print('value',value)
        # input_id = 'LSMM'
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
            # print(value)
            # print('\n')

        return wind_temp_data
    
        # Process the weather data as needed
        # print('Weather data:', weather_data)
        if 'data' not in weather_data:
            print('No data found in response')
            return None
                
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
#    except requests.exceptions.RequestException as req_err:
#       print(f'Request error occurred: {req_err}')
#  except ET.ParseError as parse_err:
#     print(f'XML parse error: {parse_err}')
    return None


def specific_data(location='Seattle',type='\'temp\''):

    hist_data = get_hist_data(location)
    type = str(type)
    # if type[1:] == "'":
    type = type[1:-1]
    print(f"this is type {type}")
    print(f'this is hist_data: {hist_data}')
    weather_dict=[]
    if not hist_data:
        # print(type)
        print(location)
        return 'No data for selected parameters'

    for data in hist_data:
        print(f"this is data in spec data {data}")
        # if type in hist_data:
        single_day = {
            'datetime': data['datetime'],
            type: data[type]
         }
        # print(single_day)
        weather_dict.append(single_day)

    return weather_dict
if __name__ == '__main__':
    specific_data('Seatte','temp')
