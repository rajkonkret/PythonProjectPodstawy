from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-06-10

time = datetime.now()
print(time)  # 2026-06-10 09:26:17.380392

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)  # 10

# formatowanie daty
formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 10/06/2026
print(type(formated_date))  # <class 'str'>

formated_time = datetime.now().strftime("%I:%M %p")
print(formated_time)  # 09:31 AM

# zmiana na obiekt
object_date = datetime.now().strptime("10/06/2026", "%d/%m/%Y")
print(object_date)  # 2026-06-10 00:00:00
print(type(object_date))  # <class 'datetime.datetime'>

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'

# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-06-11

products = [
    {'sku': 1, "exp_date": today, "price": 200},
    {'sku': 2, "exp_date": today, "price": 200},
    {'sku': 3, "exp_date": tomorrow, "price": 200},
    {'sku': 4, "exp_date": today, "price": 200},
    {'sku': 5, "exp_date": tomorrow, "price": 200},
]

for p in products:
    # print(p)
    # print(p['exp_date'])

    if p['exp_date'] != today:
        continue  # zostaw ten, wez nastepny

    p['price'] *= 0.8  # price = price * 0.8

    print(f"""
Price for sku: {p['sku']}
is now: {p['price']:.2f} pln""")

# Price for sku: 1
# is now: 160.00 pln
#
# Price for sku: 2
# is now: 160.00 pln
#
# Price for sku: 4
# is now: 160.00 pln
