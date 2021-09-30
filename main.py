from grove.factory import Factory
import time
from textwrap import wrap
import requests
from datetime import datetime
import pytz
import datetime

BASE_URL = 'https://api.open-meteo.com/v1/forecast'
DISPLAY_ID = 'JHD1802'
AMS_LAT = 52.38275
AMS_LNG = 4.8523391
ATH_LAT = 37.983810
ATH_LNG = 23.727539

WEATHER_CODES = {
    0: 'Clear sky',
    1: 'Mainly clear',
    2: 'Partly cloudy',
    3: 'Overcast',
    45: 'Fog',
    48: 'Depositing rime fog',
    51: 'Light drizzle',
    53: 'Moderate drizzle',
    55: 'Dense drizzle',
    56: 'Light freezing drizzle',
    57: 'Dense freezing drizzle',
    61: 'Slight rain',
    63: 'Moderate rain',
    65: 'Heavy rain',
    66: 'Light freezing rain',
    67: 'Heavy freezing rain',
    71: 'Slight snow fall',
    73: 'Moderate snow fall',
    75: 'Heavy snow fall',
    77: 'Snow grains',
    80: 'Slight rain showers',
    81: 'Moderate rain showers',
    82: 'Violent rain showers',
    85: 'Slight snow showers',
    86: 'Heavy snow showers',
    95: 'Slight thunderstorm',
    96: 'Slight hail',
    99: 'Heavy hail',
}
 
def weather(lat, lng):
    url = '{}?latitude={:f}&longitude={:f}&current_weather=true'.format(BASE_URL, lat, lng)

    r = requests.get(url)
    curr_weather = r.json()['current_weather']
    return {
        'temp': curr_weather['temperature'],
        'code': WEATHER_CODES[curr_weather['weathercode']],
        'windspeed': curr_weather['windspeed'],
    }

def format_temp(city, temp, weather_code):
    return '{} {} C      {}'.format(city, temp, weather_code)

def format_wind(city, wind):
    return '{} Windspeed       {} KM/H'.format(city, wind)

display = Factory.getDisplay(DISPLAY_ID)
display.clear()

while True:
    cute_messages = ['Hey lil\' bug, I love you']
    #cuteMessages.append('Insert cute message')
    #cuteMessages.append('Insert cute message')
    cute_messages.append('Hakuna matata!')

    ams_weather = weather(AMS_LAT, AMS_LNG)
    ams_date_now = datetime.datetime.now(pytz.timezone('Europe/Amsterdam'))
    ams_formatted_date = ams_date_now.strftime('AMS %d %b %Y %H:%M')

    ath_weather = weather(ATH_LAT, ATH_LNG)
    ath_date_now = datetime.datetime.now(pytz.timezone('Europe/Athens'))
    ath_formatted_date = ath_date_now.strftime('ATH %d %b %Y %H:%M')

    cute_messages.append(ams_formatted_date)
    cute_messages.append(format_temp('AMS', ams_weather['temp'],ams_weather['code'] ))
    cute_messages.append(format_wind('AMS', ams_weather['windspeed']))
    cute_messages.append(ath_formatted_date)
    cute_messages.append(format_temp('ATH', ath_weather['temp'],ath_weather['code'] ))
    cute_messages.append(format_wind('ATH', ath_weather['windspeed']))

    for message in cute_messages:
        display.clear()
        if len(message) > 32:
            display.setCursor(0,0)
            display.write('Error. Cuteness')
            display.setCursor(1,0)
            display.write('Overload')
        elif len(message) > 16:
            splitMessage = wrap(message,16)
            display.setCursor(0,0)
            display.write(splitMessage[0])
            display.setCursor(1,0)
            display.write(splitMessage[1])
        elif len(message) <= 16:
            display.setCursor(0,0)
            display.write(message)
        time.sleep(5)

    



    
