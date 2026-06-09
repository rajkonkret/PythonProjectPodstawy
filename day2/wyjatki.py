# wyjątki - błedy podczas wykonywania programu

# print(5 / 0)

try:
    # print(5 / 0)
    # int('A')
    # print(2 + "Ania")
    # raise KeyError("Błąd klucza")
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Błąd wartości")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print("Błąd:", e)  # Błąd: 'Błąd klucza'
else:  # działa tylko gdy nie ma błedu
    print("wynik:", wynik)
finally:  # wykona się zawsze
    print("Następny pacjent")


print("Program nadal działa")
# Nie dziel przez zero
# Program nadal działą
# print("wynik:", wynik)
