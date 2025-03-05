from bs4 import BeautifulSoup
import requests

# Effettuo una richiesta GET alla risorsa specificata
try:
    risorsa = requests.get("http://web-15.challs.olicyber.it/")
    risorsa.raise_for_status()
except requests.RequestException as e:
    print(f"Errore nella richiesta: {e}")
    exit(1)

# Analizzo il contenuto HTML della risorsa
soup = BeautifulSoup(risorsa.text, 'html.parser')

# Trovo e stampo tutti gli elementi <link> nella pagina
print(soup.find_all("link"))
links = []
for link in soup.find_all("link"):
    links.append(link.get("href"))
    # Effettuo una richiesta GET per ogni href trovato e stampo il contenuto
    response = requests.get("http://web-15.challs.olicyber.it/" + link.get("href")).text
    #print(response)
    # Cerco la stringa 'flag{' nel contenuto e la stampo se trovata
    if 'flag{' in response:
        print("Flag trovata:", response)

# Trovo e stampo tutti gli elementi <script> nella pagina
scripts = []
for script in soup.find_all("script"):
    scripts.append(script.get("src"))
    # Effettuo una richiesta GET per ogni src trovato e stampo il contenuto
    response = requests.get("http://web-15.challs.olicyber.it/" + script.get("src")).text
    #print(response)
    # Cerco la stringa 'flag{' nel contenuto e la stampo se trovata
    if 'flag{' in response:
        print("Flag trovata:", response)