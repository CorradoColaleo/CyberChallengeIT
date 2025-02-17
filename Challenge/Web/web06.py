import requests
s = requests.session()
s.get("http://web-06.challs.olicyber.it/token")
print(s.get("http://web-06.challs.olicyber.it/flag").content.decode("utf-8"))