from base64 import b64decode
s = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE=='
print(b64decode(s))

z = 664813035583918006462745898431981286737635929725
num_bytes = z.to_bytes((z.bit_length() + 7) // 8, byteorder='big')
print(num_bytes)
