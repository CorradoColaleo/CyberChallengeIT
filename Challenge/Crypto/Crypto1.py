def decode(text):
    decoded = []
    for letter in text:
        decoded.append(chr(letter))
    print("".join(decoded))
    
decode([102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125])