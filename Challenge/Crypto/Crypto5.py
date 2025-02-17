def xor(a, b):
    return bytes([x^b for x in a])

ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
b = bytes.fromhex(ciphertext)

for key in range(256):
    decrypted = xor(b, key)
    decrypted_text = decrypted.decode('utf-8', errors='ignore')
    print(decrypted_text)
    print("----")