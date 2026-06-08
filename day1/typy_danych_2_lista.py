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
