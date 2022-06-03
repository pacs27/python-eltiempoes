from eltiempoes import ElTiempoEs

tiempo = ElTiempoEs()
tiempo.search_location("cordoba")
data = tiempo.get_all_data_in_json(station_name="Córdoba")

print(data)