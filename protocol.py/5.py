# Добавь в словарь с параметрами weather_parameters ещё два параметра:
# M без значения — чтобы скорость ветра была в метрах в секунду, как принято у метеорологов;
# lang со значением ru, чтобы прогноз выдавался на русском языке.

import requests


url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': ''
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)