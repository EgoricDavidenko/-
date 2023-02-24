import sqlite3

con = sqlite3.connect("coffee.db")

cur = con.cursor()

result = cur.execute("""SELECT * FROM cofeyok""").fetchall()

for elem in result:
    print(elem)

con.close()

