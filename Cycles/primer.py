class Sword:

    def __init__(self, name, blade_length, grip, material='сталь'):
        self.name = name
        self.material = material
        self.blade_length = blade_length
        self.grip = grip
        self.strength = 100

        print(f'Новый меч {name} выкован!')

    def slashing_blow(self):
        self.strength -= 10
        return (f'Нанесен рубящий удар мечом {self.name}. '
                f'Радиус поражения {self.blade_length}.')

    def piercing_strike(self):
        self.strength -= 5
        return 'Нанесен пронзающий удар мечом {self.name}'

    def sharpen(self):
        self.strength = 100
        return f'Меч "{self.name}" заточен'

    def __str__(self):
        return (
            f'Меч - "{self.name}". '
            f'Выкован из материала {self.material}, '
            f'длина клинка - {self.blade_length}, '
            f'прочность - {self.strength}'
        )


katana = Sword('Верный', 1.5,
               'под хват двумя руками')
classic_sword = Sword('Дежурный', 1.2,
                      'под хват одной рукой')

print(katana.slashing_blow())

for i in range(5):
    print(classic_sword.piercing_strike())

print(katana)
print(classic_sword)
