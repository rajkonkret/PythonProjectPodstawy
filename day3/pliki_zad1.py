# działania z plikami
# filehandler

# contex manger
# with - context manager

with open("test.log", "w", encoding="utf-8") as file:
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")

# file.write("") # ValueError: I/O operation on closed file.

with open("test.log", "w",  encoding="utf-8") as file:
    file.write("Powitanie 2\n")
    file.write("Jeszcze jedno 2\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# x tworzy plik gdy nie istnieje
# with open("test.log", "x",  encoding="utf-8") as file:
#     file.write("Powitanie\n")
#     file.write("Jeszcze jedno\n")

with open("test.log", "a",  encoding="utf-8") as file:
    file.write("dodane 2\n")
    file.write("dodane jedno 2\n")
    file.write("dśodane jedno 2\n")

with open('test.log', "r", encoding="utf-8") as fh:
    lines = fh.read()

print(lines)
# Powitanie 2
# Jeszcze jedno 2
# dodane 2
# dodane jedno 2
# dśodane jedno 2