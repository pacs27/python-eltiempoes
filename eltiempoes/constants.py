MAIN_URL = "https://www.eltiempo.es/"
DETALLADA_FLAG = "detallada"
LONG_DETALLADA_FLAG = DETALLADA_FLAG + "~ROW_NUMBER_5~~TEMP_UNIT_c~~WIND_UNIT_kmh~"
POR_HORA_FLAG = "por_hora~ROW_NUMBER_6~~TEMP_UNIT_c~~WIND_UNIT_kmh~"
SEARCH_URL = "https://www.eltiempo.es/api/weatherapi/search"
DIAS_FLAG = "~ROW_NUMBER_5~~TEMP_UNIT_c~~WIND_UNIT_kmh~"


# WEB SCRAPING POSITION
DETALLADA_DATES_TAG = {"type":"div", "class_name":"m_table_weather_day_date"}
PRECIPITATION_PROBABILITY_SPAM_POSITION = 0
CLOUD_PERCENTAGE_SPAM_POSITION = 1
ULTRAVIOLET_SPAM_POSITION = 2

DAILY_DATES_TAG = {"type":"span", "class_name":"m_table_weather_day_day"}
MAX_TEMP_TAG = {"type":"span", "class_name":"m_table_weather_day_max_temp"}
MIN_TEMP_TAG = {"type":"span", "class_name":"m_table_weather_day_min_temp"}
PRECIPITATION_TAG = {"type":"div", "class_name":"m_table_weather_day_child m_table_weather_day_rain"}
WIND_SPEED_TAG = {"type":"div", "class_name":"m_table_weather_day_child m_table_weather_day_wind"}
SUNRISE_TAG = {"type":"div", "class_name":"m_table_weather_day_child m_table_weather_day_dawn"}
SUNSET_TAG = {"type":"div", "class_name":"m_table_weather_day_child m_table_weather_day_nightfall"}
