# Игра в города продолжается. Лиза покопалась в сети и нашла дополнительный список городов для игры. 
# Но у неё нет инструмента, чтобы добавить новые города в множество all_cities.
# Напиши функцию add_cities(), которая добавит элементы из списка new_cities в all_cities. 
# Метод union() для этой задачи не подходит, ведь вам нужно добавить элементы в существующее множество, 
# а не создать новое.

def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)


def add_cities(all_cities, new_cities):
    
    


# Анфиса нашла названия нескольких новых городов, 
# эти города нужно добавить в множество all_cities 
new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан' ,
    'Новосибирск'
}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)