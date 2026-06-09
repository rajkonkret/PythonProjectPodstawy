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

# zarobki = int(input("Podaj zarobki:"))
#
# podatek = 0
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.6
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# # podatek 20% dla przeziału 10000 do 39999

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")

rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")

# napisac test z ...
# trzy pytanie
# dodac punktację
#
# punkty = 0
#
# odp = input("Podaj rok Chrztu Polski")  # str
#
# if odp.strip().casefold() == '966':
#     print("Odpowiedz prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Masz to w ksiązce na str 56")
#
# # spam += 1    spam = spam + 1
# # spam -= 1    spam = spam - 1
# # spam *= 1    spam = spam * 1
# # spam /= 1    spam = spam / 1
# # spam %= 1    spam = spam % 1
#
# odp = input("W którym roku była Bitwa pod Grunwaldem")  # str
#
# if odp.strip().casefold() == '1410':
#     print("Odpowiedz prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Masz to w ksiązce na str 189")
#
# print("Punkty:", punkty)

# Podaj rok Chrztu Polski966
# Odpowiedz prawidłowa
# W którym roku była Bitwa pod Grunwaldem1410
# Odpowiedz prawidłowa
# Punkty: 2


# zasymulejemy sytem zbierania logów
# zmienna: typ systemu -> console, email, inny
# console: "Stało się coś strasznego"
# email: "system email"
# gdy system jest email:
# do listy błedów dodac tłumaczenie błedu
# poziomy błędów: error, medium, inny

lista_b = []
# alert_system = "console"
alert_system = "email"
alert_error = "error"

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if alert_error == "error":
        lista_b.append("Krytyczny")
    elif alert_error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("inny system")

print(lista_b)
# System email
# ['Krytyczny']
