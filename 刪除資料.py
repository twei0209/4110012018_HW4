# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect('BBQ.db')

cursor = conn.cursor()

cursor.execute("DELETE FROM BBQ")

cursor.execute('''
               CREATE TABLE IF NOT EXISTS BBQ(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   price INTEGER,
                   quantity INTEGER
                )''')

cursor.execute("INSERT INTO BBQ(name, price, quantity) VALUES('chicken',30,5)")
cursor.execute("INSERT INTO BBQ(name, price, quantity) VALUES('beef',55,10)")
cursor.execute("INSERT INTO BBQ(name, price, quantity) VALUES('pork',40,15)")

cursor.execute('DELETE FROM BBQ WHERE price = "40"')

cursor.execute("SELECT * FROM BBQ")
BBQ = cursor.fetchall()

print("BBQ買啥:")
for name in BBQ:
    print(name)

conn.commit()
conn.close()