import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points.
      """
print(random.randint(1, 100))  # int od 1 do 100

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.30070798177396896 od 0 do 0.9999999
print(random.random() * 8)  # 1.930552044272897 od 0 do 7.9999999

lista = [67, 45, 32, 68, 90, 42, 49]
print(lista[random.randrange(len(lista))])  # 90

print(random.choice(lista))  # losuje element z kolekcji

lista_kul = list(range(1, 50))

for _ in range(6):  # od 0 do 5
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    print(kula)
# 67
# 68
# 14
# 45
# 40
# 1
# 16
# 17

print(random.choices(lista_kul, k=6))  # [15, 36, 36, 25, 30, 6], z powtórzeniami

print(random.sample(lista_kul, k=6))  # [42, 20, 3, 1, 31, 43], bez powtórzeń
