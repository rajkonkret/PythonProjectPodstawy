# słownik - para klucz : wartość
# {"user" : "Radek"}
# klucze nie mogą się powtarzac
# {"name":"John", "age":30, "car":null}
# słownik jest odpowiednikiem jsona

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie lemntow do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz wiek
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 50])
# dict_items([('imie', 'Radek'), ('wiek', 50)])

# nadpisanie
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 50}

dictionary['imie'] = ['Radek', "Tomek", "Magda"]
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# wypisywnie
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']

# wypisac Tomek
print(dictionary['imie'][1])  # Tomek

print(dictionary['imie'][1].lower())  # Tomek
print(dictionary['imie'][::-1])  # ['Magda', 'Tomek', 'Radek']

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

print(chr(223))  # ß
# \uXXXX - Znak Unicode o wartości czteroznakowego kodu szesnastkowego
print("\u00DF")  # ß
# \N{name} - Znak Unicode o podanej nazwie
print('\N{LATIN SMALL LETTER SHARP S}')  # ß

name1 = "GROSS"
name2 = "groß"

print(name1.lower() == name2.lower())  # False
"""Casefolding is similar to lowercasing but more aggressive
 because it is intended to remove all case distinctions 
in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". """
print(name1.casefold() == name2.casefold())  # True

dictionary.update({'date': '12-12-2030'})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50, 'date': '12-12-2030'}

dict_small = {'x': 20}
dict_small.update([("y", 3), ("z", 7)])
print(dict_small)  # {'x': 20, 'y': 3, 'z': 7}


