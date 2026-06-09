# pętla - możliwosc wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for _ in range(15):
    print("Test podłoga")
    # print(_)  # 14

print("Wyjscie z pętli")

for i in range(5):
    print(i * 2)
    print(i + 2)

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzienia
        print(i, "parzysta")

# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# parzyste do listy

lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)
# [0, 2, 4, 6, 8]

for i in range(len(lista3)):  # range(5)
    print(lista3[i])

for c in lista3:  # podstawi kolejny element
    print(c)

for c in lista3:
    if c > 4:
        print(c, "Większe niż 4")
    elif c == 4:
        print("Równe 4")
    else:
        print("Mniejsze niz 4")
    print(c)  # za kazdym przejsciem pętli
print("Po zakonczeniu pętli")

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # (start, stop, krok)
    print(i)

imiona = ['Sylwia', "Kamila", "Karolina", "Monika"]

# wypisac elementy z listy jeden pod drugim

for o in imiona:
    print(o)
# Sylwia
# Kamila
# Karolina
# Monika

# 0 Sylwia

for o in imiona:
    print(imiona.index(o), o)
# 0 Sylwia
# 1 Kamila
# 2 Karolina
# 3 Monika

for i in range(len(imiona)):
    print(i, imiona[i])

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Sylwia') ->  0 Sylwia
# (1, 'Kamila')
# (2, 'Karolina')
# (3, 'Monika')
a, b = (0, 'Sylwia')
print(a, b)

for i, o in enumerate(imiona):
    print(i, o)

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Sylwia
# 2 Kamila
# 3 Karolina
# 4 Monika
