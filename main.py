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
CITY_1 = "Amsterdam"
CITY_2 = "Athens"

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
    return {
        'city': city,
        'displayed_weather': '{} C {} '.format(temp, weather_code)
    }

def format_wind(city, wind):
    return {
        'city': city,
        'displayed_wind': 'Windspeed {} KM/H '.format(wind)
    }

display = Factory.getDisplay(DISPLAY_ID)
display.clear()

cute_messages = ['Hey lil\' bug, I love you']
#cuteMessages.append('Insert cute message')
#cuteMessages.append('Insert cute message')
cute_messages.append('Hakuna matata!')

for message in range(0,len(cute_messages)):
        cute_messages[message] = 15*' '+cute_messages[message]+' '

while True:
    weather_msg_ams = []
    weather_msg_ath = []

    ams_weather = weather(AMS_LAT, AMS_LNG)
    ams_date_now = datetime.datetime.now(pytz.timezone('Europe/Amsterdam'))
    ams_formatted_date = ams_date_now.strftime('%d %b %Y %H:%M')

    ath_weather = weather(ATH_LAT, ATH_LNG)
    ath_date_now = datetime.datetime.now(pytz.timezone('Europe/Athens'))
    ath_formatted_date = ath_date_now.strftime('%d %b %Y %H:%M')

    weather_msg_ams.append(ams_formatted_date)

    fmt_weather = format_temp(CITY_1, ams_weather['temp'],ams_weather['code'] )
    weather_msg_ams.append(fmt_weather['displayed_weather'])

    fmt_wind = format_wind(CITY_1, ams_weather['windspeed'])
    weather_msg_ams.append(fmt_wind['displayed_wind'])

    weather_msg_ath.append(ath_formatted_date)

    fmt_weather = format_temp(CITY_2, ath_weather['temp'],ath_weather['code'] )
    weather_msg_ath.append(fmt_weather['displayed_weather'])

    fmt_wind = format_wind(CITY_2, ath_weather['windspeed'])
    weather_msg_ath.append(fmt_wind['displayed_wind'])

    for message in range(0,len(weather_msg_ams)):
         weather_msg_ams[message] = 15 * ' ' + weather_msg_ams[message] + ' '

    for message in range(0,len(weather_msg_ath)):
         weather_msg_ath[message] = 15 * ' ' + weather_msg_ath[message] + ' '

    #display weather
    for message in range(0, len(weather_msg_ams)):
        for letter in range(0, len(weather_msg_ams[message])):
            display.clear()
            display.setCursor(0,3)
            display.write(CITY_1)
            display.setCursor(1,0)
            display.write(weather_msg_ams[message][letter:len(weather_msg_ams[message])])
            time.sleep(0.5)

    for message in range(0, len(weather_msg_ath)):
        for letter in range(0, len(weather_msg_ath[message])):
            display.clear()
            display.setCursor(0,5)
            display.write(CITY_2)
            display.setCursor(1,0)
            display.write(weather_msg_ath[message][letter:len(weather_msg_ath[message])])
            time.sleep(0.5)

    #display cute messages
    for message in range(0,len(cute_messages)):
        for letter in range(0, len(cute_messages[message])):
            display.clear()
            display.setCursor(0,0)
            display.write('Cute msgs for U:')
            display.setCursor(1,0)            
            display.write(cute_messages[message][letter:len(cute_messages[message])])
            time.sleep(0.5)
