# zbior (set)  - przechowuje unikalne wartości
# nie zachowuje kolejnosci przy dodawaniu elementów
# nie posiada indexu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbior
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmiana kolejności
print(type(zbior))  # <class 'set'>

print(sorted(zbior))  # [11, 22, 33, 44, 55, 66, 777]

# pusty zbior
zb2 = set()  # tylko słówkiem set
print(zb2)  # set()

# dodani elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(25)
zbior.add(33)
zbior.add(33)
print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 25}

# usunięcie elemntu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 25}

# pop() - usunie pierwszy element
# ctrl shift f - wyszukiwanie w kodzie
print(zbior.pop())

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print("Zmienna:", zmienna)  # Zmienna: 66

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 25, 667, 62}
print(type(zbior_2))  # <class 'set'>

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {777, 22, 25}
print(zbior.difference(zbior_2))  # {777, 22, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zmienia bazowy
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 25, 667, 62}

krotka = tuple(zbior)
print(krotka)

lista = list(zbior)
print(lista)

# in - sprawdzenie czy elemen istnieje w kolekcji
print(667 in zbior)  # True
print(667 in lista)  # True
print(667 in krotka)  # True
print(6777 in krotka)  # False
