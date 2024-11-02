# Из таблицы ice_cream базы данных db.sqlite получите значение поля name тех записей, 
# у которых значения полей is_published и is_on_main равны TRUE.
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