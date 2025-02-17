import requests
playload = {"id":"flag"}
r=requests.get("http://web-02.challs.olicyber.it/server-records",params=playload)
print(r.content.decode("utf-8"))