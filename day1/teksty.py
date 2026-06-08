tekst = "Witaj Świecie"

print(tekst)
# Witaj Świecie

#  teksty są niemutowalne
# Return a copy of the string with all the cased characters
tekst.upper()
print(tekst)

tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie
# Witaj Świecie

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

# Witaj Świecie
# 0123456789...

print(tekst[1])  # i
print(tekst[3])  # a
print(tekst[5])  #

print(tekst.index("Ś"))  # 6
print(tekst.index("e"))  # 9, pierwszy z lewej

print(tekst.lower().count("w"))  # występujw 2 razy

# Witaj Świecie
# 0123456789...
print(tekst.count("j", 0, 4))  # -> 0123, z prawej strony ma zbiór otwarty, wystepuje 0 razy

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)
# b'Witaj \xc5\x9awiecie'
# b - bajty
print(type(encode_s))  # <class 'bytes'>
# \xc5\x9a literka Ś w kodzie szesnastkowym

print(encode_s.decode('utf-8'))
# Witaj Świecie

imie = "Radek"
print(len(imie))  # pomiar długości, 5

dane = "Świecie"
print(len(dane))  # 7

# Mam na imię .....
print("Mam na imię" + imie)  # Mam na imięRadek
print("Mam na imię", imie)  # Mam na imię Radek
print("Mam na imię", imie, sep="ooo")  # Mam na imięoooRadek

# f-string , wstrzyknięcie zawartości zmiennej do tekstu
tekst_format = f"Mam na imię {imie}"
print(tekst_format)  # Mam na imię Radek

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię pythona"
# \t - tab
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format("Radek"))  # Witaj Radek!

print("""
    witaj
Radek
""")

#     witaj
# Radek

"""
Komentarz
    wielolinijkowy (docstring)"""
