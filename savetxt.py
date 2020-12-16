import csv
import sqlite3
with open('save.txt') as fin:
    csvin = csv.reader(fin)
    for row in csvin:
        print ( ','.join(row[:5]), ','.join(row[5:]))

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS mytable(var1 TEXT, var2 INT, var3 Bool)''')


with open("save.txt", "r") as f:
    rows = f.readlines()
    for row in rows:
        fields = row.split(',')
        c.execute(f'INSERT INTO mytable (var1, var2, var3)'\
                  f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}')")

conn.commit()

for row in c.execute('SELECT * FROM myTable'):
    print(row)

conn.close()