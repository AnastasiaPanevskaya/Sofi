# Заполни таблицу ice_cream данными из списка кортежей ice_cream.
# Таблица с полями name, description и category уже  создана.

import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

ice_cream = [
    ('Пивное мороженое',
     'Со вкусом светлого нефильтрованного лагера',
     'Экзотическое',
     ),
    ('Мороженое с кузнечиками',
     'В колумбийском стиле: с добавлением карамелизованных кузнечиков.',
     'Экзотическое',
     ),
    ('Мороженое со вкусом сыра чеддер',
     'Вкус настоящего сыра в вафельном стаканчике.',
     'Экзотическое',
     ),
    ('Пломбир 1937',
     'Пломбир по рецепту 1937 года Московского хладокомбината',
     'Обычное'
     ),
]


con.commit()
con.close()