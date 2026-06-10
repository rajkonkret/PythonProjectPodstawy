import csv

# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,9Chrząszczyżewoszyce
# csv - dane oddzielone znakiem podziału - ,;tab|

row = ['radek', 'coe', "3", 0]
fields = ['name', 'branch', 'year', 'cgpa']

filename = 'records.csv'

# newline="" - ominięcie problemu pustych linii
with open(filename, "w", newline="") as csv_f:
    csv_writer = csv.writer(csv_f)
    csv_writer.writerow(fields)
    csv_writer.writerow(row)

dict_name = dict(zip(fields, row))
print(dict_name)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}

filename = "records_dict.csv"
with open(filename, "w", newline="") as f:
    csv_writer = csv.DictWriter(f, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerow(dict_name)

products = [
    {'sku': 1, "exp_date": 'today', "price": 200},
    {'sku': 2, "exp_date": 'today', "price": 200},
    {'sku': 3, "exp_date": 'tomorrow', "price": 200},
    {'sku': 4, "exp_date": 'today', "price": 200},
    {'sku': 5, "exp_date": 'tomorrow', "price": 200},
]

list_product = [key for key in products[0]]
print(list_product)

filename = "records_discount.csv"
with open(filename, "w", newline="") as f:
    csv_writer = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csv_writer.writeheader()
    csv_writer.writerows(products)  # writerows - lista słowników
