# заготовлена база данных db.sqlite с таблицей ice_cream.
# Получите из этой таблицы результирующую выборку, которая
# содержит значения столбцов name и text...
# …тех записей, у которых значение поля is_published равно True,
# отсортирована по полю name в обратном алфавитном порядке,
# содержит две записи, начиная со второй.

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напиши SQL запрос в строке.
cur.execute('''

''')


for result in cur:
    print(result)


con.commit()
con.close()