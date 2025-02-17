import requests
playload = {"username":"admin","password":"admin"}
print(requests.post("http://web-08.challs.olicyber.it/login",data=playload).text)