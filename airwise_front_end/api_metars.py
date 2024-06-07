#!/usr/bin/env python3

import requests
import json

def get_metar(ids="@WA", format="json", taf="1", hours="10", bbox="40,-90,45,-85", date="20240531_144001Z"):
    base_url = "http://www.aviationweather.gov/api/data/metar"
    params = {
        'ids': ids,
        'format': format,
        'taf': taf,
        'hours': hours,
        'bbox': bbox,
        'date': date,
    }

    headers = {"Accept": "application/json"}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        #print("Response content:", response.content)
        # If response content is empty or not valid JSON, handle it
        if not response.content:
            print("Empty response")
            return None
        try:
            weather_data = json.loads(response.content)
        except ValueError:
            print("Response is not valid JSON")
            return None
        
        metar_data = []
        for site in weather_data:
            metar = {
                "metar_id": site.get('metar_id'),
                "icaoId": site.get('icaoId'),
                "receiptTime": site.get('receiptTime'),
                "obsTime": site.get('obsTime'),
                "reportTime": site.get('reportTime'),
                "temp": site.get('temp'),
                "dewp": site.get('dewp'),
                "wdir": site.get('wdir'),
                "wspd": site.get('wspd'),
                "visibility": site.get('visib'),
                "altim": site.get('altim'),
                "slp": site.get('slp'),
                "qcField": site.get('qcField'),
                "wxString": site.get('wxString'),
                "presTend": site.get('presTend'),
                "maxT": site.get('maxT'),
                "minT": site.get('minT'),
                "maxT24": site.get('maxT24'),
                "minT24": site.get('minT24'),
                "precip": site.get('precip'),
                "pcp3hr": site.get('pcp3hr'),
                "pcp6hr": site.get('pcp6hr'),
                "pcp24hr": site.get('pcp24hr'),
                "metarType": site.get('metarType'),
                "raw0b": site.get('raw0b'),
                "name": site.get('name'),
                "elev": site.get('elev'),
                "prior": site.get('prior'),
                "mostRecent": site.get('mostRecent'),
                "cover": site.get('cover'),
                "base": site.get('base'),
            }
            metar_data.append(metar)
        return metar_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    return None
if __name__ == "__main__":
# Example usage
    metar_data = get_metar(ids="@WA", format="json", taf="1", hours="10", bbox="40,-90,45,-85", date="20240531_144001Z")
    if metar_data:
        for metar in metar_data:
            print(f"METAR ID: {metar['metar_id']}, ICAO ID: {metar['icaoId']}, "
                f"Receipt Time: {metar['receiptTime']}, Observation Time: {metar['obsTime']}, "
                f"Report Time: {metar['reportTime']}, Temp: {metar['temp']}C, "
                f"Dew Point: {metar['dewp']}C, Wind Direction: {metar['wdir']} degrees, "
                f"Wind Speed: {metar['wspd']} kt, Visibility: {metar['visibility']} statute miles, "
                f"Altimeter: {metar['altim']} inHg, Sea Level Pressure: {metar['slp']} mb, "
                f"Quality Control Field: {metar['qcField']}, Weather String: {metar['wxString']}, "
                f"Pressure Tendency: {metar['presTend']}, Max Temp: {metar['maxT']}C, Min Temp: {metar['minT']}C, "
                f"Max Temp (24hr): {metar['maxT24']}C, Min Temp (24hr): {metar['minT24']}C, "
                f"Precipitation: {metar['precip']} in, Precip (3hr): {metar['pcp3hr']} in, "
                f"Precip (6hr): {metar['pcp6hr']} in, Precip (24hr): {metar['pcp24hr']} in, "
                f"METAR Type: {metar['metarType']}, Raw Observation: {metar['raw0b']}, "
                f"Name: {metar['name']}, Elevation: {metar['elev']} ft, Prior: {metar['prior']}, "
                f"Most Recent: {metar['mostRecent']}, Cover: {metar['cover']}, Base: {metar['base']} ft")
    else:
        print("No data available")
