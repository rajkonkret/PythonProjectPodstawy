import chardet

# pip install chardet

# odczyt binarny rb
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Powitanie 2\r\nJeszcze jedno 2\r\ndodane 2\r\ndodane jedno 2\r\nd\xc5\x9bodane jedno 2\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.8308108108108109, 'language': 'pl', 'mime_type': 'text/plain'}
# {'encoding': 'utf-8', 'confidence': 0.86, 'language': 'pl', 'mime_type': 'text/plain'}
encoding = result['encoding']

print(50 * "-")
print(raw_data.decode(encoding=encoding))
# --------------------------------------------------
# Powitanie 2
# Jeszcze jedno 2
# dodane 2
# dodane jedno 2
# dśodane jedno 2
