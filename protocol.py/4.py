# Запроси погодный сервис http://wttr.in по URL без параметров.
# А их задай словарём weather_parameters.
# Функция get() должна принимать его, как отдельный аргумент params

import requests


url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = ...  # передайте параметры в http-запрос

print(response.text)