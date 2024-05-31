#!/usr/bin/env python3

import requests, json, os
from datetime import date, timedelta

def get_raw_weather_data(location='Seattle', current_state='future'):
    api_key = 'EBBMX4R5X9X9EYAYQ4S9FNDS4'
    city = location+',USA'
    end_date = date.today()
    start_date=date.today() - timedelta(days=5)

    # print('thia ia current state',current_state)
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={api_key}'
    if current_state == 'past':
        # print('I am in past')
        url =f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?key={api_key}'
        # print('this is url',url)

    # url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?locations={location}&aggregateHours=24&unitGroup=us&shortColumnNames=false&contentType=csv&key={api_key}'

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
            print('Empty response')
            return None
        # weather_data = ""
        # Attempt to parse the JSON response
        try:
            weather_data = response.json()
            return weather_data
            # print('this is weather data', weather_data)
            
            
            # print('\n')
        except ValueError:
            print('Response is not valid JSON')
            return None

        # value = weather_data.get('id')
        # value = weather_data['icaoID']
        # print('value',value)
        # input_id = 'LSMM'
        # Process the weather data as needed
    # print('Weather data:', weather_data)
        if 'data' not in weather_data:
            print('No data found in response')
            return None
            
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    #    except requests.exceptions.RequestException as req_err:
    #       print(f'Request error occurred: {req_err}')
    #  except ET.ParseError as parse_err:
    #     print(f'XML parse error: {parse_err}')
    print("this is weather data in get_hist_data",weather_data)
    


def filter_weather_data(location='Seattle',current_state='future'):
    weather_data = get_raw_weather_data(location, current_state)
    # print(f"This is weather data in filter weather {weather_data}")
    if weather_data is None:
        return 'No data for selected parameters'
    # print(f"This is weather data in get weather {weather_data}")
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


def get_past_data(location='Seattle',type='\'temp\'', past=True):
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

def specific_data(location='Seattle',type='\'temp\'', current_state='future'):
    
    if current_state[0] == "'":
        current_state = current_state[1:-1]
    
    forecast_data = filter_weather_data(location, current_state)
    type = str(type)
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



if __name__ == '__main__':
    # specific_data('Seatte','\'temp\'')
    specific_data('Seatte','temp', 'past')
    # forecast_data('Seatte')    pass