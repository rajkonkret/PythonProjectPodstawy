dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wypisanie wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "<==>", v)
# imie <==> Radek
# nazwisko <==> Kowalski

for k, v in dictionary.items():
    print(k, v, sep="<==>")
# imie<==>Radek
# nazwisko<==>Kowalski

pol_ang = {'pies': 'dog', "kot": 'cat', "dach": "roof"}

# zrobic słownik ang_pol
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k

print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
