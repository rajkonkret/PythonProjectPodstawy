# od pythona 3.10
# match case

lista = []

lang = input("Podaj znany Ci język progamowania:")

match lang.strip().casefold():
    case "python":
        lista.append("znam Pythona")
    case "java":
        lista.append("znam Jave")
    case "c":
        lista.append("Znam C")
    case _:  # odpowiednik else
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język progamowania:java
# ['znam Jave']
