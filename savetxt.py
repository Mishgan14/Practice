import csv

with open('save.txt') as fin:
    csvin = csv.reader(fin)
    for row in csvin:
        print ( ','.join(row[:5]), ','.join(row[5:]))