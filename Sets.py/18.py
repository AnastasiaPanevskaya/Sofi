# Допиши в конец программы вызов функции process_lisa() с аргументом 'Где все мои друзья?'.
# В теле функции process_lisa() добавь ещё одно условие elif, которое будет проверять, 
# содержит ли переменная query строку 'Где все мои друзья?'. 
# В теле нового блока elif пока что напиши return 'Я поняла, это вопрос про города!'
# Запусти код, удостоверьтесь, что Лиза поняла запрос.

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_lisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверь, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей - 
        # перебери словарь DATABASE в цикле
        for friend in DATABASE:     
            friends_string += friend + ' '     # Добавляй к переменной friends_string имя друга и пробел
        # Верни строку, составленную из 'Твои друзья: ' и friends_string 
        return('Твои друзья: ' + friends_string)  
    else:
        return '<неизвестный запрос>'

# Не изменяй следующий код
print('Привет, я Лиза!')
print(process_lisa('Сколько у меня друзей?'))
print(process_lisa('Кто все мои друзья?'))