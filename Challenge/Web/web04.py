import requests

#con cambio di formato
headers={'Accept':'application/xml'}
print(requests.get("http://web-04.challs.olicyber.it/users",headers=headers).content.decode("utf-8"))

print("--------------------------")

#Senza cambio di formato
print(requests.get("http://web-04.challs.olicyber.it/users").content.decode("utf-8"))