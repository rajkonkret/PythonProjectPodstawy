import json

# json - dane typu klucz - wartosc
# typ wymiany danych klient - serwer
# odpowiednikiem jsona jest słownik
# zawsze podwójny cudzysłów
# None -> null

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)
print(type(person_dict))  # <class 'dict'>

# zapis danych jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify - upiekszanie
with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)

# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowanie po kluczu
with open('nasze_dane_s.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>

print("Imie pacjenta:", data['name'])  # Imie pacjenta: Radek

# zamiana słownika na json (tekst)
json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

# zamiana na słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
print("Imie pacjenta:", dict_json['name'])  # Imie pacjenta: Radek
