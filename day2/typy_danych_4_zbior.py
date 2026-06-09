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


