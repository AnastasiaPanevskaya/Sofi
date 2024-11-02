# Посчитай в таблице ice_cream базы db.sqlite среднюю цену тех сортов мороженого,
# у которых в поле category стоит значение «Экзотическое».

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
results = cur.execute('''

''')

for result in results:
    print(result)

con.close()