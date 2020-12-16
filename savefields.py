
with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()



with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(information)

FILENAME = "word.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], row[1])