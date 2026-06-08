user = "Tomek"  # str
wiek = 39  # int

wersja = 3.90001
print(type(wersja))  # <class 'float'>, zmiennoprzecnkowe

liczba = 8909871234321345678  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.

# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

#
print(f"witaj {user}, masz teraz {wiek} lat.")
# witaj Tomek, masz teraz 39 lat.

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3)  # Używamy wersji Pythona 3.00
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 - zaokrągla
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4 - zaokrągla

print(f"Używamy wersji Pythona {wersja}")
print(f"Używamy wersji Pythona {wersja:.2f}")
print(f"Używamy wersji Pythona {wersja:.1f}")
print(f"Używamy wersji Pythona {wersja:.0f}")
# Używamy wersji Pythona 3.90001
# Używamy wersji Pythona 3.90
# Używamy wersji Pythona 3.9
# Używamy wersji Pythona 4

print(wersja)  # 3.90001

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>15}")  # "          Tomek"
print(f"{user:^15}")  # "     Tomek     "
print(f"{user:.^15}")  # ".....Tomek....."
