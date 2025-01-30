#Christine Mier
#October 15, 2024
#weather module which opens and adds to json file and outputs it as a Historical and daily report

import json
import os
import calendar

data = {}

def read_data(*, filename):
    '''Opens json file'''
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        return {}

def write_data(*, data, filename):
    '''writes in json file'''
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4)

def max_temperature(*, data, date):
    '''returns max temp'''
    temperatures = [reading['t'] for key, reading in data.items() if key.startswith(date)]
    return max(temperatures) if temperatures else None
def min_temperature(*, data, date):
    '''returns min temp'''
    temperatures = [reading['t'] for key, reading in data.items() if key.startswith(date)]
    return min(temperatures) if temperatures else None

def max_humidity(data, date):
    '''maximum humidity'''
    humidities = [reading['h'] for key, reading in data.items() if key.startswith(date)]
    return max(humidities) if humidities else None

def min_humidity(*, data, date):
    '''minimum humidity'''
    humidities = [reading['h'] for key, reading in data.items() if key.startswith(date)]
    return min(humidities) if humidities else None

def tot_rain(*, data, date):
    '''total rainfall'''
    rainfall = [reading['r'] for key, reading in data.items() if key.startswith(date)]
    return sum(rainfall) if rainfall else 0.0

def report_daily(*, data, date):
    '''Generates Daily Weather Report'''
    report_format = []
    report_format.append("==============================DAILY REPORT==============================")
    report_format.append(f'{"Date":22}{"Time":10}{"Temp":8}{"Humidity":10}{"Rainfall":10}')
    report_format.append("========================================================================")

    month_index = int(date[4:6])
    if 1 <= month_index <= 12:
        for key in sorted(data.keys()):
            if key.startswith(date):
                time = key[8:14]
                temp = data[key]['t']
                hum = data[key]['h']
                rain = data[key]['r']
                month = calendar.month_name[int(date[4:6])]
                report_format.append(f'{month} {date[6:8]}, {date[:4]}{' '*5} {time}{' '*5} {temp}{' '*5} {hum}{' '*5} {rain:.2f}')
        return "\n".join(report_format)

def report_historical(*, data):
    '''Generates Historical Weather Report'''
    report_format = []
    report_format.append("==============================HISTORICAL REPORT==============================")
    report_format.append(f'{" ":22}{"Minimum":15}{"Maximum":15}{"Minimum":15}{"Maximum":15}{"Total":10}')
    report_format.append(f'{"Date":22}{"Temperature":15}{"Temperature":15}{"Humidity":15}{"Humidity":15}{"Rainfall":10}')
    report_format.append("=============================================================================")
    dates = set(key[:8] for key in data.keys())
    for date in sorted(dates):
        month_index = int(date[4:6])
        if 1 <= month_index <= 12:
            month = calendar.month_name[int(date[4:6])]
            max_temp = max_temperature(data = data, date = date)
            min_temp = min_temperature(data = data, date = date)
            max_hum = max_humidity(data = data, date = date)
            min_hum = min_humidity(data = data, date = date)
            total_rain = tot_rain(data = data, date = date)

            report_format.append(f"{month} {date[6:8]}, {date[:4]}{' '*10} {min_temp}{' '*10} {max_temp}{' '*10} {min_hum}{' '*12} {max_hum}{' '*10} {total_rain:.2f}")
        else:
             print(f"Warning: Invalid month '{date[4:6]}' in date '{date}'. Skipping this entry.")
    
    return "\n".join(report_format)
