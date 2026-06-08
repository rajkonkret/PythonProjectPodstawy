# pep8 - zasady czystego kodu
# snake_case
# ctrl alt l - formatowanie

print("Hello World")  # wypisz/wydrukuj
print('Witaj Świecie')

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\Szkolenie\PycharmProjects\PythonProjectPodstawy\day1\pierwszy.py", line 8
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 8)
# Process finished with exit code 1

print("Dalsza część")

print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
# ctrl d- powielanie linijki

print('"Radek"')  # "Radek"
print('Radek \"Radek\"')  # Radek "Radek"

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe, string

print("39" + "90")  # 3990

print(39 + 90)  # 129
print(type(39))  # <class 'int'>, integer, liczba całkowita

# print("39" + 30)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie
print(int("39") + 30)  # 69 - int()  rzutowanie na liczby całkowite

print(30 * "39")
# 393939393939393939393939393939393939393939393939393939393939

print("Radek" + str(1))  # Radek1

# typowanie dynamiczne

# zmienna - pudełko na dane
name = "Radek"
print(name)
print(type(name))
# Radek
# <class 'str'>

name = 90
print(name)
print(type(name))
# 90
# <class 'int'>

# podpowiedzi typów
name: str = "Radek"
print(name)

name = 90
print(name)
# Process finished with exit code 0 - program dziala bez błędu
#  pip install mypy
# (.venv) PS C:\Users\Szkolenie\PycharmProjects\PythonProjectPodstawy> cd .\day1\
# (.venv) PS C:\Users\Szkolenie\PycharmProjects\PythonProjectPodstawy\day1> mypy .\pierwszy.py
# pierwszy.py:58: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:65: error: Name "name" already defined on line 52  [no-redef]
# pierwszy.py:68: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\Szkolenie\PycharmProjects\PythonProjectPodstawy\day1>
