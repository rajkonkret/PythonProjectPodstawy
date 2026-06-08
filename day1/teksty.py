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
