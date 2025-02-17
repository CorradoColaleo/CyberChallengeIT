import requests
headers={'X-Password':'admin'}
print(requests.get("http://web-03.challs.olicyber.it/flag",headers=headers).content.decode("utf-8"))