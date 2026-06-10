import csv

filename = 'records.csv'
# filename = 'records_discount.csv'

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect.quotechar)

    csv_f.seek(0) # ustaw odczyt na początek
    # csv_reader = csv.reader(csv_f, delimiter=";")
    csv_reader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csv_reader)  # <_csv.reader object at 0x000001B9883C8700>

    fields = next(csv_reader)  # odczyta jeden wiersz, ustawi odczyt na nastepny

    for row in csv_reader:  # ruszy od kolejnego wiersza
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
