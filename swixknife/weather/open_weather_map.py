

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from .weather import SezimalWeather
from . import functions
from ..json import json

import os
import requests


def get_weather_conditions(api_key: str, latitude: float = None, longitude: float = None, time_zone: str | ZoneInfo = None) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    req = requests.get(url)

    observation = json.loads(req.text)

    if 'main' in observation:
        observation['main']['temp'] = functions.convert_temperature_kelvin(observation['main']['temp'])
        observation['main']['feels_like'] = functions.convert_temperature_kelvin(observation['main']['feels_like'])
        observation['main']['temp_min'] = functions.convert_temperature_kelvin(observation['main']['temp_min'])
        observation['main']['temp_max'] = functions.convert_temperature_kelvin(observation['main']['temp_max'])
        observation['main']['pressure'] = functions.convert_pressure(observation['main']['pressure'])
        observation['main']['humidity'] = functions.convert_percentage(observation['main']['humidity'])
        observation['main']['sea_level'] = functions.convert_pressure(observation['main']['sea_level'])
        observation['main']['grnd_level'] = functions.convert_pressure(observation['main']['grnd_level'])

    if 'visibility' in observation:
        observation['visibility'] = functions.convert_distance(observation['visibility'])

    if 'wind' in observation['weather']:
        observation['wind']['speed'] = functions.convert_speed(observation['wind']['speed'])
        observation['wind']['gust'] = functions.convert_speed(observation['wind']['gust'])

    #
    # Save this reading for future reference
    #
    observation['api_type'] = 'open_weather_map'
    filename = os.path.expanduser('~/.sweather.json')
    open(filename, 'w').write(json.dumps(observation))

    return observation


def fill_sezimal_weather(weather: SezimalWeather, conditions: dict):
    if 'temp' in conditions['main']:
        weather._temperature = conditions['main']['temp']

    if 'feels_like' in conditions['main']:
        weather._temperature_sensation = conditions['main']['feels_like']

    if 'temp_max' in conditions['main']:
        weather._temperature_maximum = conditions['main']['temp_max']

    if 'temp_min' in conditions['main']:
        weather._temperature_minimum = conditions['main']['temp_min']

    if 'wind' in conditions:
        wind = conditions['wind']

        if 'speed' in wind:
            weather._wind_speed = wind['speed']

        if 'gust' in wind:
            weather._wind_speed = wind['gust']

        if 'deg' in wind:
            weather._wind_direction = wind['deg']

    if 'humidity' in conditions['main']:
        weather._humidity = conditions['main']['humidity']

    if 'visibility' in conditions:
        weather._visibility = conditions['visibility']

    if 'pressure' in conditions['main']:
        pressure = conditions['main']

        if 'grnd_level' in pressure:
            weather._pressure = pressure['grnd_level']

        if 'sea_level' in pressure:
            weather._pressure_sea_level = pressure['sea_level']
