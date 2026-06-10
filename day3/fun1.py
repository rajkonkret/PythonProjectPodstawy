# funkcja - blok programu, który można uzyci wielokrotnie
# funcja musi byc najpierw zadeklarowana
# zeby funkcja się uruchomiła musimy ją wywołac

a = 6
b = 8


# dekalracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(3, 8)  # 11

odejmij(1, 2)
odejmij(1, 2, 8)

odejmij(c=90, b=67, a=78)  # -79
odejmij(90, 67, c=78)  # -55

wyn = odejmij(5, 7)
print(wyn)  # None


# funkcje zwracające wynik
def odejmij2(a, b, c=0):
    return a - b - c


wyn = odejmij2(4, 9)
print(wyn)  # -5

# funkcja lambda
# skrocony zapis funkcji
# zwraca wynik
odejmij4 = lambda a, b, c=0: a - b - c
wyn = odejmij4(4, 9)
print(wyn)  # -5

lista = [6, 9, 10]

# mapowanie danych

l1 = []
for i in lista:
    l1.append(i * 2)

print(l1)  # [12, 18, 20]

# map(), filter(), reduce()
# lamda jako funkcja anonimowa
print(f"Użycie map(): {list(map(lambda x: x * 2, lista))}")
# Użycie map(): [12, 18, 20]