# while - pętla sterowana warunkiem

# pętla nieskonczona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)

print(50 * "-")
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

# Komunikat 2 !!
# 11
# --------------------------------------------------
# Komunikat 3 !!!

# password = input("Podaj hasło:")
# while password != "secret":  # != - różne
#     password = input("Podaj hasło:")
# # Podaj hasło:asadsad
# # Podaj hasło:asdadfasfa
# # Podaj hasło:dsadfadfd
# # Podaj hasło:secret
#
# while (password := input("Podaj hasło:")) != "secret":
#     pass
# # Podaj hasło:secret
# # Podaj hasło:secret

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]

while 5 in my_list:
    my_list.remove(5)

print(my_list)  # [1, 2, 3, 4, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}

print(list(dict.fromkeys(my_list)))  # [1, 5, 2, 3, 4, 6]
