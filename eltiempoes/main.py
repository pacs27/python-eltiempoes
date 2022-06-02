import json
from unidecode import unidecode
from typing import Dict, Tuple, List, Union
from requests import get
from bs4 import BeautifulSoup, ResultSet

from .utils.create_urls import create_prediction_url, create_search_url
from .web_scraping import (
    get_precipitation_probabilities,
    get_cloud_percentages,
    get_ultraviolet_radiations,
    get_detallada_dates,
    get_daily_dates,
    get_max_temperatures,
    get_min_temperatures,
    get_precipitations,
    get_winds_speed,
    get_sunrise_hours,
    get_sunset_hours,
)


class ElTiempoEs:
    def __init__(self):
        pass

    def search_location(
        self, location_name: str, limit: int = 100
    ) -> List[Dict[str, Union[str, int, float]]]:
        """Search for all stations of the given name

        Args:
            location_name (str): Any name of a location. For example: "Córdoba"
            limit (int, optional): Maximum number of results returned. Defaults to 100.

        Returns:
            List[Dict[str, Union[str, int, float]]]: Results with stations data
        """
        search_url = create_search_url(name=location_name, lim=limit)
        response_data = get(search_url)
        response_text_data = response_data.text
        response_text_data_in_json = json.loads(response_text_data)
        return response_text_data_in_json

    def _get_daily_prediction(
        self, estacion_name: str
    ) -> Tuple[
        List[Tuple[int, str]],
        List[int],
        List[int],
        List[float],
        List[int],
        List[str],
        List[str],
    ]:
        """Gets the daily forecast over a 14-day period.

        Args:
            estacion_name (str): Station name (must be the same as the urlize fiel in the station json data)

        Returns:
                Tuple[
                    dates: List[Tuple[int, str]]]
                    max_temperature: List[int]
                    min_temperature: List[int]
                    precipitation: List[float]
                    wind_speed: List[int]
                    sunrise: List[str]
                    sunset: List[str]
                ]
        """
        estacion_name = unidecode(estacion_name)
        estacion_name_lowercase = estacion_name.lower()

        daily_url = create_prediction_url(
            estacion=estacion_name_lowercase, prediction_type="dias"
        )
        response_data = get(daily_url)
        response_data_text = response_data.text
        soup = BeautifulSoup(response_data_text, "html.parser")

        dates = get_daily_dates(soup)
        max_temperature = get_max_temperatures(soup)
        min_temperature = get_min_temperatures(soup)
        precipitation = get_precipitations(soup)
        wind_speed = get_winds_speed(soup)
        sunrise = get_sunrise_hours(soup)
        sunset = get_sunset_hours(soup)
        return (
            dates,
            max_temperature,
            min_temperature,
            precipitation,
            wind_speed,
            sunrise,
            sunset,
        )

    def _get_daily_prediction_json(self, estacion_name: str) -> List[Dict[str, object]]:
        """Gets the daily forecast over a 14-day period in json format.

        Args:
            estacion_name (str): Station name (must be the same as the urlize fiel in the station json data)

        Returns:
             List[
                 Dict[
                    "date": Tuple[int, str]]
                    "max_temperature": int; degrees Celsius
                    "min_temperature": int; degrees Celsius
                    "precipitation": float;  mm
                    "wind_speed": int;  km/h
                    "sunrise_hour": str
                    "sunset_hour": str
                ]
            ]
        """
        (
            dates,
            max_temperature,
            min_temperature,
            precipitation,
            wind_speed,
            sunrise,
            sunset,
        ) = self._get_daily_prediction(estacion_name=estacion_name)

        daily_items_json = []
        for index, item in enumerate(dates):
            item_dict = {
                "date": item,
                "max_temperature": max_temperature[index],
                "min_temperature": min_temperature[index],
                "precipitation": precipitation[index],
                "wind_speed": wind_speed[index],
                "sunrise": sunrise[index],
                "sunset": sunset[index],
            }
            daily_items_json.append(item_dict)

        return daily_items_json

    def _get_detallada_prediction(
        self, estacion_name: str
    ) -> Tuple[List[Tuple[int, str]], List[float], List[float], List[str]]:
        """Gets the detallada daily forecast over a 14-day period.

        Args:
            estacion_name (str): Station name (must be the same as the urlize fiel in the station json data)

        Returns:
                Tuple[
                    dates: List[Tuple[int, str]]]
                    precipitation_probability: List[float] in percentage of one
                    cloud_percentage: List[float] in percentage of one
                    ultraviolet_radiation: List[str]
                ]
        """
        estacion_name = unidecode(estacion_name)
        estacion_name_lowercase = estacion_name.lower()

        detallada_url = create_prediction_url(
            estacion=estacion_name_lowercase, prediction_type="detallada"
        )
        response_data = get(detallada_url)
        response_data_text = response_data.text
        soup = BeautifulSoup(response_data_text, "html.parser")

        dates = get_detallada_dates(soup)
        precipitation_probability = get_precipitation_probabilities(soup)
        cloud_percentage = get_cloud_percentages(soup)
        ultraviolet_radiation = get_ultraviolet_radiations(soup)
        return (
            dates,
            precipitation_probability,
            cloud_percentage,
            ultraviolet_radiation,
        )

    def _get_detallada_prediction_json(
        self, estacion_name: str
    ) -> List[Dict[str, object]]:
        """Gets the detallada daily forecast over a 14-day period in json format.

        Args:
            estacion_name (str): Station name (must be the same as the urlize fiel in the station json data)

        Returns:
             List[
                 Dict[
                    "date": Tuple[int, str]]
                    "precipitation_probability": float in percentage of one
                    "cloud_percentage": float in percentage of one
                    "ultraviolet_radiation": str
                ]
            ]
        """
        (
            dates,
            precipitation_probability,
            cloud_percentage,
            ultraviolet_radiation,
        ) = self._get_detallada_prediction(estacion_name=estacion_name)

        detallada_items_json = []
        for index, item in enumerate(dates):
            item_dict = {
                "date": item,
                "precipitation_probability": precipitation_probability[index],
                "cloud_percentage": cloud_percentage[index],
                "ultraviolet_radiation": ultraviolet_radiation[index],
            }
            detallada_items_json.append(item_dict)

        return detallada_items_json

    def get_all_data_in_json(self, estacion_name: str) -> List[Dict[str, object]]:
        """Gets all daily forecast data over a 14-day period in json format.

        Args:
            estacion_name (str): Station name (must be the same as the urlize fiel in the station json data)

        Returns:
             List[
                 Dict[
                    "date": Tuple[int, str]]
                    "max_temperature": int; degrees Celsius
                    "min_temperature": int; degrees Celsius
                    "precipitation": float;  mm
                    "wind_speed": int;  km/h
                    "sunrise_hour": sunride hour in the format (%hh/%mm)
                    "sunset_hour": sinset hour in the format (%hh/%mm)
                    "precipitation_probability": float; in percentage of one
                    "cloud_percentage": float; in percentage of one
                    "ultraviolet_radiation": str; List of texts with differents radiation types, like ('Muy alta' ...)
            }
                ]
            ]
        """
        (
            dates_detallada,
            precipitation_probability,
            cloud_percentage,
            ultraviolet_radiation,
        ) = self._get_detallada_prediction(estacion_name=estacion_name)

        (
            dates_daily,
            max_temperature,
            min_temperature,
            precipitation,
            wind_speed,
            sunrise,
            sunset,
        ) = self._get_daily_prediction(estacion_name=estacion_name)
        all_json_items = []
        if len(precipitation_probability) < 14:
            # TODO: This sometimes happens. Have a look
            raise Exception("It is not possible to connect with eltiempo.es/detallada.")
        for index, item in enumerate(dates_daily):
            item_dict = {
                "date": item,
                "max_temperature": max_temperature[index],
                "min_temperature": min_temperature[index],
                "precipitation": precipitation[index],
                "wind_speed": wind_speed[index],
                "sunrise": sunrise[index],
                "sunset": sunset[index],
                "precipitation_probability": precipitation_probability[index],
                "cloud_percentage": cloud_percentage[index],
                "ultraviolet_radiation": ultraviolet_radiation[index],
            }
            all_json_items.append(item_dict)

        return all_json_items
