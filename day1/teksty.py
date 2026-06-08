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
