# Удали из кода строку return 'Я поняла, это вопрос про города!':
# на этом месте нужно написать код, который
# создаст перечень городов из словаря DATABASE (города в этом перечне не должны повторяться);
# вернёт фразу Твои друзья в городах: <город_1> <город_2> <город_3> ... 
# (города должны перечисляться через пробел).

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_friends(friends_count):
    if friends_count == 1:
        return 'У тебя 1 друг'
    elif 2 <= friends_count <= 4:
        return 'У тебя ' + str(friends_count) + ' друга'
    elif friends_count >= 5:
        return 'У тебя ' + str(friends_count) + ' друзей'


def process_query(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return format_friends(count)
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return 'Твои друзья: ' + friends_string
    else:
        return '<неизвестный запрос>'


def runner():
    print('Привет, я Лиза!')
    print(process_query('Сколько у меня друзей?'))
    print(process_query('Кто все мои друзья?'))
    print(process_query('Где все мои друзья?'))



runner()