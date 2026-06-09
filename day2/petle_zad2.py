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
