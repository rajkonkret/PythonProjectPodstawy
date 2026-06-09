# krotka - kolekcja niemutowalna (tylko do odczytu)
# pozwala efektywniej zarzadzac pamięcią

tupla_imiona = "Zenek", "Tomek", "Marek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Tomek', 'Marek', 'Ania')

tupla_liczby = (43, 45, 22.34, 11, 200)
tupla_liczby = 43, 45, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 45, 22.34, 11, 200)

# tupla jednoelementowa
tupla_jeden = (45,)  # pep8 tu zaleca nawias
print(tupla_jeden)
print(type(tupla_jeden))

# tupla_liczby[0] = 123
# TypeError: 'tuple' object does not support item assignment

# usunięcie całej krotki
del tupla_liczby
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona)
print(tupla_imiona.index("Zenek"))  # indeks numer 0
print(tupla_imiona.count("Zenek"))  # wystepuje 1 raz

print(len(tupla_imiona))  # długość 4

tup = 1, 2

# a - pierwszy element
# b - drugi element
a = tup[0]
b = tup[1]

print(a, b)  # 1 2

# rozpakowanie krotki
a, b = tup
print(a, b)  # 1 2

# zamiana wartości zmiennych miejscami
a, b = b, a
print(a, b)  # 2 1

print(tupla_imiona)  # ('Zenek', 'Tomek', 'Marek', 'Ania')
# name1, name2, name3
# * dowolna ilosc elementow
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)
# Zenek ['Tomek', 'Marek'] Ania

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)
# ['Zenek', 'Tomek'] Marek Ania

# sorted() - sortowanie, zwracaposortowaną listę
print(sorted(tupla_imiona))
print(tupla_imiona)  # nie zmmienia oryginału

sortowana = sorted(tupla_imiona)
print(sortowana)  # ['Ania', 'Marek', 'Tomek', 'Zenek']

lista = list(tupla_imiona)
print(lista)  # ['Zenek', 'Tomek', 'Marek', 'Ania']
