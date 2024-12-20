# Напиши функцию what_weather(), которую затем будешь использовать в коде Лизы:
# Выполни HTTP-запрос, поместив вызов функции get() внутрь блока try.
# Значения URL и параметров получи из функций make_url() (в неё нужно передать нужный город как аргумент city)
# и make_parameters().
# При «выбрасывании» исключения типа requests.ConnectionError — функция what_weather() 
# должна возвращать сообщение об ошибке '<сетевая ошибка>'.
# Если код HTTP-ответа равен 200 (всё хорошо), верни из функции текст ответа.
# В противном случае функция должна вернуть строку '<ошибка на сервере погоды>'.

import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    # Напишите тело этой функции.
    # Не изменяйте остальной код!

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))