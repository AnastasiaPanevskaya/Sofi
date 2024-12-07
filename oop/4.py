# Метод родительского класса describe даёт очень скудное описание птиц. Исправим это.
# Для метода describe в родительском классе добавился параметр
# full со значением по умолчанию False.
# Ваша задача — переопределить этот метод для каждого дочернего класса: 
# если параметр full равен False, метод должен возвращать стандартное описание птицы из родительского класса;
# если параметр full равен True, метод должен возвращать полное описание птицы.
# Полное описание для класса Parrot :
# Попугай name — заметная птица, окрас её перьев — color,
# а размер — size. Интересный факт: попугаи чувствуют ритм,
# а вовсе не бездумно двигаются под музыку. Если сменить композицию, то и темп движений птицы изменится.
# Полное описание для класса Рenguin:
# Размер пингвина name из рода genus — size.
# Интересный факт: однажды группа геологов-разведчиков похитила пингвинье яйцо,
# и их принялась преследовать вся стая, не пытаясь, впрочем, при этом нападать.
# Посовещавшись, похитители вернули птицам яйцо, и те отстали.

class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    # describe



class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    # describe
        
            


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe(False)
kowalski.describe(True)