import requests

#print(requests.options("http://web-10.challs.olicyber.it/").headers)

#noto che sono supportate head, options e get -> provo con post

print(requests.post("http://web-10.challs.olicyber.it/").headers)
