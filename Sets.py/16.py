# Перед поездкой в командировку будет полезно покопаться в записной книжке и выяснить 
# — а кто из друзей живёт в том городе, куда предстоит поехать. Кто покажет город лучше, чем местный житель?
# Научи Лизу анализировать список друзей и определять, живёт ли кто-нибудь из друзей в пункте назначения. 
# Для  этого напиши функцию is_anyone_in(collection, city). 
# Для каждого неподходящего города функция должна напечатать фразу
# В городе <название_города> у меня есть друг, но мне туда не надо.
# Если кто-то из друзей живёт в запрошенном городе — функция должна напечатать фразу 
# В городе <название_города> живёт <имя_друга>. Обязательно зайду в гости!

friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь'
}

def is_anyone_in(collection, city):
#    for friend in ...
#        if ...
            print(...)
#        else:
            print(...)
    
is_anyone_in(friends, 'Хабаровск')