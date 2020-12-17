from typing import Optional
from sqlfastai import FastAPI
import uvicorn
import csv
import sys
import MySQLdb
app = FastAPI()

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

@app.get("/{word}/int/bool")
def read_item(word: Optional[str] = {fields[0]}, q: int = {fields[1]}, w: bool = {fields[2]} ):
    print(f"word: {word}  q: {q} w:{w}")
    return {"word": word, "q": q, "w": w}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)