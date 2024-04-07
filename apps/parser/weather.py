import requests


def get_weather(city):
    api_key = '28c8e715bdb5d5bb438b2d1051508faa'  # замените 'your_api_key_here' на ваш API ключ OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.0/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Извлекаем нужные данные о погоде из JSON
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    else:
        print("Ошибка при получении данных о погоде:", response.status_code)
        return None, None


# Город, для которого мы хотим получить данные о погоде
city = input("Введите название города: ")

temperature, description = get_weather(city)

if temperature is not None and description is not None:
    print(f"Текущая температура в городе {city}: {temperature}°C")
    print(f"Погодные условия: {description}")

#Это часть для проверки кода
