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
