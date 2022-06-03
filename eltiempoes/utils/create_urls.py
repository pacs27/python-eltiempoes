# -*- coding: utf-8 -*-

from typing import Literal

from eltiempoes.constants import MAIN_URL, DIAS_FLAG, DETALLADA_FLAG, LONG_DETALLADA_FLAG, POR_HORA_FLAG, SEARCH_URL

# https://www.eltiempo.es/api/weatherapi/search?q=cordoba&lim=100&country=es
# https://www.eltiempo.es/cordoba.html
# https://www.eltiempo.es/cordoba.html~ROW_NUMBER_5~~TEMP_UNIT_c~~WIND_UNIT_kmh~
# https://www.eltiempo.es/cordoba.html?v=detallada~ROW_NUMBER_5~~TEMP_UNIT_c~~WIND_UNIT_kmh~
# https://www.eltiempo.es/cordoba.html?v=por_hora~ROW_NUMBER_6~~TEMP_UNIT_c~~WIND_UNIT_kmh~
# https://www.eltiempo.es/ajax-maps-v2?principal=es&navigator=desktop&day=20220531&hour=1
# https://www.eltiempo.es/api/v1/get_current_conditions_by_pelmorex_id/ESXX0007


def create_prediction_url(
    estacion: str, prediction_type: Literal["dias", "detallada", "long_detallada", "por_hora"] = "dias"
) -> str:
    if prediction_type == "detallada":
        return f"{MAIN_URL}{estacion}.html?v={DETALLADA_FLAG}"
    elif prediction_type == "long_detallada":
        return f"{MAIN_URL}{estacion}.html?v={LONG_DETALLADA_FLAG}"
    elif prediction_type == "por_hora":
        return f"{MAIN_URL}{estacion}.html?v={POR_HORA_FLAG}"
    elif prediction_type == "dias":
        return f"{MAIN_URL}{estacion}.html{DIAS_FLAG}"
    else:
        raise Exception(f"type '{prediction_type}' is not supported.await")


def create_search_url(name: str, lim: int = 100, country: str = "es") -> str:
    url = f"{SEARCH_URL}?q={name}&lim={lim}&contry={country}"
    return url
