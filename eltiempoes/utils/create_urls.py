from typing import Literal
from ..constants import *

# https://www.eltiempo.es/api/weatherapi/search?q=cordoba&lim=100&country=es
# https://www.eltiempo.es/cordoba.html
# https://www.eltiempo.es/cordoba.html~ROW_NUMBER_5~~TEMP_UNIT_c~~WIND_UNIT_kmh~
# https://www.eltiempo.es/cordoba.html?v=detallada~ROW_NUMBER_5~~TEMP_UNIT_c~~WIND_UNIT_kmh~
# https://www.eltiempo.es/cordoba.html?v=por_hora~ROW_NUMBER_6~~TEMP_UNIT_c~~WIND_UNIT_kmh~
# https://www.eltiempo.es/ajax-maps-v2?principal=es&navigator=desktop&day=20220531&hour=1


def create_prediction_url(
    estacion: str, type: Literal["dias", "detallada", "por_hora"] = "dias"
) -> str:
    if type == "detallada":
        return f"{MAIN_URL}{estacion}.html?v={DETALLADA_FLAG}"
    elif type == "por_hora":
        return f"{MAIN_URL}{estacion}.html?v={POR_HORA_FLAG}"
    elif type == "dias":
        return f"{MAIN_URL}{estacion}.html{DIAS_FLAG}"
    else:
        raise Exception(f"type '{type}' is not supported.await")


def create_search_url(name: str, lim: int = 100, country: str = "es") -> str:
    url = f"{SEARCH_URL}?q={name}&lim={lim}&contry={country}"
    return url
