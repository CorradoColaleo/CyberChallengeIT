from bs4 import BeautifulSoup, Comment
import requests

try:
    risorsa = requests.get("http://web-14.challs.olicyber.it/")
    risorsa.raise_for_status() 
except requests.RequestException as e:
    print(f"Errore nella richiesta: {e}")
    exit(1)

soup = BeautifulSoup(risorsa.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

if comments:
    for comment in comments:
        print(f"Commento trovato: {comment}")
        if "flag" in comment:
            try:
                flag = comment.split(":")[1].strip()
                print(f"Flag trovato: {flag}")
            except IndexError:
                print("Errore nel parsing del commento: il commento non contiene la flag nel formato previsto.")
else:
    print("Nessun commento trovato nella pagina.")