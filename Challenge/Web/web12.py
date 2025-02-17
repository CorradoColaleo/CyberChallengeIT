import requests
from bs4 import BeautifulSoup

risorsa = requests.get("http://web-12.challs.olicyber.it/")
soup = BeautifulSoup(risorsa.text, 'html.parser')
print(soup.find_all('p'))