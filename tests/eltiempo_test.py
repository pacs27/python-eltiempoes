from eltiempoes import ElTiempoEs

tiempo = ElTiempoEs()

data = tiempo.get_detallada_prediction(estacion_name="Córdoba")

print(data)