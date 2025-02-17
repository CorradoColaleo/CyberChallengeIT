def decode(x):
    res = bytes.fromhex(x)
    return res.decode("ascii")
    
print(decode("666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"))