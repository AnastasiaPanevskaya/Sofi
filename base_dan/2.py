# В базе данных db.sqlite создай таблицу ice_cream с полями name, description и category. 
# Все поля должны хранить данные типа «строка».

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()