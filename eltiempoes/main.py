import json

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
