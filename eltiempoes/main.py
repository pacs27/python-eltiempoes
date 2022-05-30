import json
from unidecode import unidecode
from typing import List

from requests import get
from bs4 import BeautifulSoup

from .constants import *
from .utils.create_urls import create_prediction_url, create_search_url


class ElTiempoEs:
    def __init__(self):
        pass

    def search_location(self, location_name: str, limit: int = 100):
        search_url = create_search_url(name=location_name, lim=limit)
        response_data = get(search_url)
        response_text_data = response_data.text
        response_text_data_in_json = json.loads(response_text_data)
        return response_text_data_in_json

    def get_daily_prediction(self, estacion_name: str):
        estacion_name = unidecode(estacion_name)
        estacion_name_lowercase = estacion_name.lower()

        daily_url = create_prediction_url(
            estacion=estacion_name_lowercase, prediction_type="dias"
        )
        response_data = get(daily_url)
        response_data_text = response_data.text
        soup = BeautifulSoup(response_data_text, "html.parser")
        dates = get_dates_daily(soup)
        max_temperature = get_max_temperature(soup)
        min_temperature = get_min_temperature(soup)
        precipitation = get_precipitation(soup)
        wind_speed = get_wind_speed(soup)
        sunrise = get_sunrise(soup)
        sunset = get_sunset(soup)
        return (
            max_temperature,
            min_temperature,
            precipitation,
            wind_speed,
            sunrise,
            sunset,
        )
        
    def get_detallada_prediction(self, estacion_name: str):
        estacion_name = unidecode(estacion_name)
        estacion_name_lowercase = estacion_name.lower()

        detallada_url = create_prediction_url(
            estacion=estacion_name_lowercase, prediction_type="detallada"
        )
        response_data = get(detallada_url)
        response_data_text = response_data.text
        soup = BeautifulSoup(response_data_text, "html.parser")
        dates = get_dates(soup)
        precipitation_probability = get_precipitation_probability(soup)
        cloud_percentage = get_cloud_percentage(soup)
        ultraviolet_radiation = get_ultraviolet_radiation(soup)

        return dates


def get_precipitation_probability(html_text: BeautifulSoup) -> List[int]:
    precipitation_probability_soup = html_text.findAll(attrs={"data-expand-tablechild-item":True})
    precipitation_probability = []
    for precipitation_probability_item in precipitation_probability_soup:
        precipitation_probability.append(precipitation_probability_item.find_all('span')[0].text.split()[0])
    return precipitation_probability

def get_cloud_percentage(html_text: BeautifulSoup) -> List[int]:
    cloud_percentage_soup = html_text.findAll(attrs={"data-expand-tablechild-item":True})
    cloud_percentage = []
    for cloud_percentage_item in cloud_percentage_soup:
        cloud_percentage.append(cloud_percentage_item.find_all('span')[1].text.split()[0])
    return cloud_percentage

def get_ultraviolet_radiation(html_text: BeautifulSoup) -> List[int]:
    ultraviolet_radiation_soup = html_text.findAll(attrs={"data-expand-tablechild-item":True})
    ultraviolet_radiation = []
    for ultraviolet_radiation_item in ultraviolet_radiation_soup:
        ultraviolet_radiation.append(ultraviolet_radiation_item.find_all('span')[2].text)
    return ultraviolet_radiation

def get_dates(html_text: BeautifulSoup) -> List[int]:
    date_soup = html_text.findAll(
        "span", class_="m_table_weather_day_day"
    )
    date = []
    for date_item in date_soup:
        date.append((date_item.text.split()[0],date_item.text.split()[1]))
    return date


def get_max_temperature(html_text: BeautifulSoup) -> List[int]:
    max_temperature_soup = html_text.findAll(
        "span", class_="m_table_weather_day_max_temp"
    )
    max_temperature = []
    for max_temperature_item in max_temperature_soup:
        max_temperature.append(int(max_temperature_item.span["data-temp"]))
    return max_temperature


def get_min_temperature(html_text: BeautifulSoup) -> List[int]:
    min_temperature_soup = html_text.findAll(
        "span", class_="m_table_weather_day_min_temp"
    )
    min_temperature = []
    for min_temperature_item in min_temperature_soup:
        min_temperature.append(int(min_temperature_item.span["data-temp"]))
    return min_temperature


def get_precipitation(html_text: BeautifulSoup) -> List[float]:
    precipitation_soup = html_text.findAll(
        "div", class_="m_table_weather_day_child m_table_weather_day_rain"
    )
    precipitation = []
    for precipitation_item in precipitation_soup:
        precipitation.append(
            float(precipitation_item.findAll("span")[1].text.split()[0])
        )
    return precipitation


def get_wind_speed(html_text: BeautifulSoup) -> List[int]:
    wind_speed_soup = html_text.findAll(
        "div", class_="m_table_weather_day_child m_table_weather_day_wind"
    )
    wind_speed = []
    for wind_speed_item in wind_speed_soup:
        wind_speed.append(
            int(wind_speed_item.findAll("span")[1].find("span").text.split()[0])
        )
    return wind_speed


def get_sunrise(html_text: BeautifulSoup) -> List[int]:
    sunrise_soup = html_text.findAll(
        "div", class_="m_table_weather_day_child m_table_weather_day_dawn"
    )
    sunrise = []
    for sunrise_item in sunrise_soup:
        sunrise.append(sunrise_item.findAll("span")[1].text.split()[0])
    return sunrise


def get_sunset(html_text: BeautifulSoup) -> List[int]:
    sunset_soup = html_text.findAll(
        "div", class_="m_table_weather_day_child m_table_weather_day_nightfall"
    )
    sunset = []
    for sunset_item in sunset_soup:
        sunset.append(sunset_item.findAll("span")[1].text.split()[0])
    return sunset
