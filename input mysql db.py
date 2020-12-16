
import MySQLdb
import csv
import sys



mydb = MySQLdb.connect(host='192.168.10.123', port=6033,
    user='root',
    passwd='my_secret_password',
    db='app_db')
cursor = mydb.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS mytable(var1 TEXT, var2 INT, var3 Bool)''')
try:
    file = open(sys.argv[1])
except IOError as e:
    print(u'не удалось открыть файл')
else:
    with file:
        print(u'Файл существует')
with open(sys.argv[1], "r") as f:
    rows = f.readlines()
    for row in rows:
        fields = row.split(',')
        cursor.execute(f'INSERT INTO mytable (var1, var2, var3)'\
                  f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}')")

mydb.commit()


