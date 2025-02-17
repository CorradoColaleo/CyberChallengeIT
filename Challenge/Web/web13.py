import requests
from bs4 import BeautifulSoup

risorsa = requests.get("http://web-13.challs.olicyber.it/")
soup = BeautifulSoup(risorsa.text, 'html.parser')
highlighted_letters = soup.find_all("span", class_="red") 
flag = "".join(span.text for span in highlighted_letters)
final_flag = f"flag{{{flag}}}"
print("Flag trovata:", final_flag)