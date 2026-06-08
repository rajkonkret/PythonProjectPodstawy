# kolekcje

# lista - przechowuje dowolną ilość danych, różnego typu na raz
# zachowuje kolejnośc przy dodawaniu eleemntów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))
print(pusta_lista)
# <class 'list'>
# []

# dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Zenek")
lista.append("Karolina")
lista.append("Monika")
print(lista)
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Karolina', 'Monika']

print(len(lista))  # 6 elementów

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Karolina', 'Monika']
#    0         1        2        3        4           5

print(lista[1])
print(lista[3])
print(lista[5])
# Tomek
# Zenek
# Monika

# print(lista[10])  # IndexError: list index out of range

# ostatni element
print(lista[5])  # Monika
print(lista[len(lista) - 1])  # Monika
print(lista[-1])  # Monika
print(lista[-2])  # Karolina
print(lista[-3])  # Zenek

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Karolina', 'Monika']
#    0         1        2        3        4           5
#    -6        -5       -4       -3       -2          -1

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Marek'] 012
print(lista[:3])  # ['Radek', 'Tomek', 'Marek']

print(lista[2:])  # ['Marek', 'Zenek', 'Karolina', 'Monika'], z osttanim włąćznie
print(lista[2:5])  # ['Marek', 'Zenek', 'Karolina'] bez ostatniego!

print(lista[2:10])  # ['Marek', 'Zenek', 'Karolina', 'Monika']
print(lista[12:26])  # []

print(lista[:])
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Karolina', 'Monika']

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Karolina', 'Monika']
#    0         1        2        3        4           5
#    -6        -5       -4       -3       -2          -1

print(lista[-2:0])  # [] [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Marek', 'Zenek'] [0:4]

# 0 do 14
# range()
lista_15 = list(range(15))
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(lista_15[::-1])
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista_15[::-2])  # [14, 12, 10, 8, 6, 4, 2, 0]

print(list(range(0, 15, 2)))  # (start, stop, krok) [0, 2, 4, 6, 8, 10, 12, 14]
# range(15) od 0 do 14
# range(0, 15) od 0 do 14

tablica = [[1, 2], [3, 4]]
print(tablica)  # [[1, 2], [3, 4]]
# numpy - tablice/macierze

print(lista)
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Karolina', 'Monika']

# podmiana elementu
lista[2] = "Sylwia"
print(lista)
# ['Radek', 'Tomek', 'Sylwia', 'Zenek', 'Karolina', 'Monika']

# dopisanie w konkretne miejsce
lista.insert(1, "Kamila")
print(lista)
# ['Radek', 'Kamila', 'Tomek', 'Sylwia', 'Zenek', 'Karolina', 'Monika']

lista.append("Radek")
print(lista)
# ['Radek', 'Kamila', 'Tomek', 'Sylwia', 'Zenek', 'Karolina', 'Monika', 'Radek']

# usunięcie elemntu, pierwszy z lewej
lista.remove("Radek")
print(lista)
# ['Kamila', 'Tomek', 'Sylwia', 'Zenek', 'Karolina', 'Monika', 'Radek']

# usunięcie po indeksie
print(lista.pop(3))  # Zenek

print(lista.pop(-1))  # Radek

print(lista)
print(lista.pop())  # Monika, usunie ostatni element

# sprawdzenie indeksu elementu
print(lista.index("Sylwia"))  # index numer 2

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3

b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # kopia referencji, adresu
lista_copy = lista.copy()  # kopia eleemntów listy

print(lista2)  # ['Kamila', 'Tomek', 'Sylwia', 'Karolina']
print(lista)  # ['Kamila', 'Tomek', 'Sylwia', 'Karolina']

lista.clear()  # kasuje wszystkie lementy z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Kamila', 'Tomek', 'Sylwia', 'Karolina']

liczby = [54, 999, 12.34, 34, 567, 999]
print(liczby)  # [54, 999, 12.34, 34, 567, 999]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)
# [12.34, 34, 54, 567, 999, 999]

liczby.append("A")
print(liczby)  # [12.34, 34, 54, 567, 999, 999, 'A']
print(type(liczby))  # <class 'list'>

# liczby.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Kamila', 'Tomek', 'Sylwia', 'Karolina']
lista_copy.sort()
print(lista_copy)  # ['Kamila', 'Karolina', 'Sylwia', 'Tomek']

lista_copy.sort(reverse=True)
print(lista_copy)
# ['Tomek', 'Sylwia', 'Karolina', 'Kamila']

lista_copy.append("Tomek")
print(lista_copy)  # ['Tomek', 'Sylwia', 'Karolina', 'Kamila', 'Tomek']
lista_copy.reverse()
print(lista_copy)  # ['Tomek', 'Kamila', 'Karolina', 'Sylwia', 'Tomek'], tylko odwrócenie

print(liczby)
print(liczby[0:3])
liczby[3] = 666
print(liczby[-3])
print(liczby)

tekst = "Pyth on."

lista = [tekst]
print(lista)  # ['Pyth on.']

# rozpakowanie sekwencji
lista_tekst = list(tekst)
print(lista_tekst)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Tomek', 'Kamila', 'Karolina', 'Sylwia', 'Tomek')
