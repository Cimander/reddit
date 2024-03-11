from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('28c8e715bdb5d5bb438b2d1051508faa')
mgr = owm.weather_manager()

# Получите данные о погоде для заданного местоположения (например, Лондон, Великобритания)
observation = mgr.weather_at_place('London,GB')
w = observation.weather

# Получите детали о погоде
print("Статус:", w.detailed_status)
print("Ветер:", w.wind())
print("Влажность:", w.humidity)
print("Температура:", w.temperature('celsius'))
print("Осадки:", w.rain)
print("Индекс теплового комфорта:", w.heat_index)
print("Облачность:", w.clouds)

