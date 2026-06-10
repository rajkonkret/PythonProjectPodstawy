# klasa - przepis
# obiekt - zbudowany wg kalsy

# CamelCase
class Human:
    """
    Klasa Human
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def wypisz_imie(self):
        print(f"Mam na imię: {self.imie}")


cz1 = Human("Radek", 50, "m")
print(cz1.wiek)
print(cz1.plec)
print(cz1.imie)

print(cz1.wypisz_imie())  # Mam na imię: Radek

# 50
# m
# Radek
print(Human.__doc__)
