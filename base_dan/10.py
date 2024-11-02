# заготовлена база данных db.sqlite с таблицей ice_cream. Цены хранятся в поле price.
# Узнай среднюю цену мороженого для каждой категории (по столбцу category)

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''

''')


for result in cur:
    print(result)


con.commit()
con.close()