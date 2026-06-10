import pandas

#  pip install pandas

data = pandas.read_csv('records_discount.csv', delimiter=";")

print(data)
#    sku  exp_date  price
# 0    1     today    200
# 1    2     today    200
# 2    3  tomorrow    200
# 3    4     today    200
# 4    5  tomorrow    200

print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='str')
#
print(data.items())

#    sku  exp_date  price
# 0    1     today    200
# 1    2     today    200
# 2    3  tomorrow    200
# 3    4     today    200
# 4    5  tomorrow    200
# Index(['sku', 'exp_date', 'price'], dtype='str')
# <generator object DataFrame.items at 0x0000013E8EE0E940>
