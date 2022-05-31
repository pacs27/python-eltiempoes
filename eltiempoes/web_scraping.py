from sqlite3 import DataError
from typing import List, Tuple 

from .constants import (
    DETALLADA_DATES_TAG,
    PRECIPITATION_PROBABILITY_SPAM_POSITION,
    CLOUD_PERCENTAGE_SPAM_POSITION,
    ULTRAVIOLET_SPAM_POSITION,
    DAILY_DATES_TAG,
    MAX_TEMP_TAG,
    MIN_TEMP_TAG,
    PRECIPITATION_TAG,
    WIND_SPEED_TAG,
    SUNRISE_TAG,
    SUNSET_TAG,
)

from bs4 import BeautifulSoup, ResultSet


def get_all_rows_table(html_text: BeautifulSoup):
    """GET ALL THE TABLE ROWS IN THE WEB PAGE

    Args:
        html_text (BeautifulSoup): HTML PAGE

    Returns:
        _type_: LIST WITH ALL THE HTML ROWS
    """
    rows_table_soup = html_text.findAll(attrs={"data-expand-tablechild-item": True})
    return rows_table_soup


def find_text_with_class_name(
    html_text: BeautifulSoup,
    tag: str,
    class_name: str,
):
    """FIND A TEXT USING THE TAG AND THE CLASS NAME

    Args:
        html_text (BeautifulSoup): HTML PAGE
        tag (str): TAG NAME (div, spam ...)
        class_name (str): CLASS NAME

    Returns:
        _type_: LIST WITH THE TEXT INSIDE THE TAGS
    """
    rows_table_soup = get_all_rows_table(html_text)
    items = []
    for row in rows_table_soup:
        item = row.find(tag, class_=class_name)
        if item:
            items.append(item.text)

    return items


def find_text_with_spam_position(
    html_text: BeautifulSoup,
    spam_position: int,
):
    """FIND TEXT USING THE SPAM POSITION INSIDE THE ROW

    Args:
        html_text (BeautifulSoup): HTML PAGE
        spam_position (int): POSITION OF THE SPAM TAG

    Returns:
        _type_: TEXT IN THIS POSITION
    """
    rows_table_soup = get_all_rows_table(html_text)

    items = []
    for row in rows_table_soup:
        item = row.find_all("span")[spam_position]
        if item:
            items.append(item.text)

    return items

def get_detallada_dates(html_text: BeautifulSoup) ->List[Tuple[int, str]]:
    """DATES FROM THE DETALLADA PAGE

    Args:
        html_text (BeautifulSoup): HTML PAGE

    Returns:
        List[Tuple[int, str]]: DATES WITH THE FORMAT (%dd, %Month)
            %Month is an str like (Jan, Feb ...) 
    """
    dates = find_text_with_class_name(
        html_text, DETALLADA_DATES_TAG["type"], DETALLADA_DATES_TAG["class_name"]
    )
    dates_fixed = [(int(date.split()[1]), date.split()[2]) for date in dates]

    return dates_fixed

def get_precipitation_probabilities(html_text: BeautifulSoup) -> List[float]:
    """Get the precipitation porbabilities in percentages of one

    Args:
        html_text (BeautifulSoup): HTML page

    Returns:
        List[float]: List with all the precipitation porbabilities in percentages of one
    """
    precipitation_probabilities = find_text_with_spam_position(
        html_text, PRECIPITATION_PROBABILITY_SPAM_POSITION
    )
    
    precipitation_probabilities_fixed = [float(precipitation_probability.split()[0][:-1])/100 for precipitation_probability in precipitation_probabilities]
    return precipitation_probabilities_fixed


def get_cloud_percentages(html_text: BeautifulSoup) -> List[float]:
    """Get percentage of clouds in percentages of one

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[float]: Percentage of clouds in percentages of one
 
    """
    cloud_percentages = find_text_with_spam_position(
        html_text, CLOUD_PERCENTAGE_SPAM_POSITION
    )
    cloud_percentages_fixed = [float(cloud_percentage.split()[0][:-1])/100 for cloud_percentage in cloud_percentages]

    return cloud_percentages_fixed


def get_ultraviolet_radiations(html_text: BeautifulSoup) -> List[str]:
    """Get ultraviolet radiation 

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[str]: List of texts with differents radiation types, like ('Muy alta' ...)
    """
    ultraviolet_radiation = find_text_with_spam_position(
        html_text, ULTRAVIOLET_SPAM_POSITION
    )

    return ultraviolet_radiation



def get_daily_dates(html_text: BeautifulSoup) -> List[Tuple[int, str]]:
    """DATES FROM THE DAILY PAGE

    Args:
        html_text (BeautifulSoup): HTML PAGE

    Returns:
        List[Tuple[int, str]]: DATES WITH THE FORMAT (%dd, %Month)
            %Month is an str like (Jan, Feb ...) 
    """
    dates = find_text_with_class_name(
        html_text, DAILY_DATES_TAG["type"], DAILY_DATES_TAG["class_name"]
    )
    
    dates_fixed = [(int(date.split()[0]), date.split()[1]) for date in dates]
        
    return dates_fixed


def get_max_temperatures(html_text: BeautifulSoup) -> List[int]:
    """Get max day temperature

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[int]: List of max day temperature in degree Celsius
    """
    max_temperatures = find_text_with_class_name(
        html_text, MAX_TEMP_TAG["type"], MAX_TEMP_TAG["class_name"]
    )
    
    max_temperatures_fixed = [int(max_temperature.split()[0][:-1]) for max_temperature in max_temperatures]
    return max_temperatures_fixed


def get_min_temperatures(html_text: BeautifulSoup) -> List[int]:
    """Get min day temperature

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[int]: List of min day temperature in degree Celsius
    """
    min_temperatures = find_text_with_class_name(
        html_text, MIN_TEMP_TAG["type"], MIN_TEMP_TAG["class_name"]
    )
     
    min_temperatures_fixed = [int(min_temperature.split()[0][:-1]) for min_temperature in min_temperatures]
    return min_temperatures_fixed


def get_precipitations(html_text: BeautifulSoup) -> List[float]:
    """Get the precipitiation 

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[float]: Water precipitation sheet in millimetres
    """

    precipitations = find_text_with_class_name(
        html_text, PRECIPITATION_TAG["type"], PRECIPITATION_TAG["class_name"]
    )

    precipitations_fixed = [float(precipitation.split()[1]) for precipitation in precipitations]
    return precipitations_fixed


def get_winds_speed(html_text: BeautifulSoup) -> List[int]:
    """Get the wind speed

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[int]: Wind speed in km/h
    """
    winds_speed = find_text_with_class_name(
        html_text, WIND_SPEED_TAG["type"], WIND_SPEED_TAG["class_name"]
    )
    
    wind_speed_fixed = [int(wind_speed.split()[1]) for wind_speed in winds_speed]
    return wind_speed_fixed


def get_sunrise_hours(html_text: BeautifulSoup) -> List[str]:
    """Sunrise Hour

    Args:
        html_text (BeautifulSoup): html page

    Returns:
        List[str]: sunride hour in the format (%hh/%mm)
    """

    sunrise_hours = find_text_with_class_name(
        html_text, SUNRISE_TAG["type"], SUNRISE_TAG["class_name"]
    )
    sunrise_hours_fixed = [sunrise_hour.split()[0] for sunrise_hour in sunrise_hours]
    return sunrise_hours_fixed


def get_sunset_hours(html_text: BeautifulSoup) -> List[str]:

    sunset_hours = find_text_with_class_name(
        html_text, SUNSET_TAG["type"], SUNSET_TAG["class_name"]
    )
    sunset_hours_fixed = [sunset_hour.split()[0] for sunset_hour in sunset_hours]
    return sunset_hours_fixed
