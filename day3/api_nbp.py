import requests

# GET - pobieranie danych

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)
print(response)
# <Response [200]>
# 2xx - ok
# 3xx - warning, przekierownie
# 4xx - 404 brak strony, 400 Bad Request problem z parametrami
# 5xx - błąd serwera np 500 Internal Server Error

print(response.text)

dane = response.json()
print(type(dane))
print(dane)  # <class 'dict'>
# {'table': 'A', 'currency': 'euro',
# 'code': 'EUR', 'rates': [
# {'no': '110/A/NBP/2026', 'effectiveDate': '2026-06-10', 'mid': 4.2481}
# ]}

for k in dane:
    print(k)

# table
# currency
# code
# rates
print("Waluta:", dane['currency'])  # Waluta: euro

print("Kurs:", dane['rates'][0]['mid'])  # Kurs: 4.2481
