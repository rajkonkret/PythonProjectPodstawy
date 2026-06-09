# instrukcja warunkowa

# if
# w zaleznosci od warunkuwykona jeden lub drugi blok programu
#

odp = True

if odp: print("Test")  # Test

if odp:
    # blok programu wykonany gdy warunek True
    print("Test")

# debugger - narzedzie do wykonywania kodu krok po kroku
# pułapki - miejsce gdzie program się zatrzyma

# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"
if odp:
    print("Dane zostały wczytane")
    # Dane zostały wczytane

if odp == "Radek":  # == - porównanie
    print("Jestem Radek")  # Jestem Radek

odp = 0
if odp:
    print("Działa")
else:  # w innym przypadku, wartosc domyślna
    print("Zero -> False")
# Zero -> False

a = "Radek"
# jezeli długosc tekstu jest większa niz 3 wypisac:
# "długos wynosi: wartośc, więcej niż 3"

if len(a) > 3:
    print(f"Długośc wynosi: {len(a)}, więcej niz 3")

n = len(a)
if n > 3:
    print(f"Długośc wynosi: {n}, więcej niz 3")
# Długośc wynosi: 5, więcej niz 3

# operator morsa, walrus operator
if (n := len(a)) > 3:
    print(f"Długośc wynosi: {n}, więcej niz 3")

# pobrac zarobki
# jesli zarobki mniejsze od 10000 podatek 0
# dla pozostałych podatek 90% (0.9)
# wypisac obliczony podaek

zarobki = int(input("Podaj zarobki:"))

podatek = 0
if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.6
else:
    podatek = 0.9

print(f"Podatek wynosi: {zarobki * podatek} pln.")
# podatek 20% dla przeziału 10000 do 39999
