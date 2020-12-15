# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

with open("hello.txt", "w") as file:
    file.write("hello world")
with open("hello.txt", "a") as file:
        file.write("\ngood bye, world")
with open("hello.txt", "a") as hello_file:
            print("\nHello, world", file=hello_file)
#with open("hello.txt", "r") as file:
#    for line in file:
 #       print(line, end="")
#with open("hello.txt", "r") as file:
 #   str1 = file.readline()
#    print(str1, end="")
 #   str2 = file.readline()
 #   print(str2, end="")
  #  str3 = file.readline()
#    print(str3)
with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()