import random
import requests
import datetime
import concurrent.futures

RESET = "\033[0m"
VERT = "\033[92m"
ROUGE = "\033[91m"

ascii_art = r'''
                                ▄████▓██   ██▓ ███▄ ▄███▓ ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
                               ██▒ ▀█▒▒██  ██▒▓██▒▀█▀ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
                              ▒██░▄▄▄░ ▒██ ██░▓██    ▓██░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
                              ░▓█  ██▓ ░ ▐██▓░▒██    ▒██ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
                              ░▒▓███▀▒ ░ ██▒▓░▒██▒   ░██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
                               ░▒   ▒   ██▒▒▒ ░ ▒░   ░  ░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
                                ░   ░ ▓██ ░▒░ ░  ░      ░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
                              ░ ░   ░ ▒ ▒ ░░  ░      ░   ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
                                    ░ ░ ░            ░       ░ ░                  ░ ░      ░ ░      ░  ░      ░  
                                      ░ ░                                                                        
'''

def obtenir_heure_actuelle():
    now = datetime.datetime.now()
    return f"{ROUGE}[{RESET}{now.strftime('%H:%M:%S')}{ROUGE}]{RESET}"

def generer_lien_nitro():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    code = "".join(random.choices(caracteres, k=16))
    api_url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}"
    lien_affiche = f"https://discord.gift/{code}"
    return api_url, lien_affiche

def verifier_nitro(api_url, lien_affiche):
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            print(f"{obtenir_heure_actuelle()} [{VERT}VALID{RESET}]  {ROUGE}->{RESET} {lien_affiche} {VERT}[200]{RESET}")
        else:
            print(f"{obtenir_heure_actuelle()} [{ROUGE}INVALID{RESET}]  {ROUGE}->{RESET} {lien_affiche} {ROUGE}[403]{RESET}")
    except requests.exceptions.RequestException:
        print(f"{obtenir_heure_actuelle()} [{ROUGE}ERROR{RESET}]  {ROUGE}->{RESET} {lien_affiche} {ROUGE}[FAILED]{RESET}")

print(f"{ROUGE}{ascii_art}{RESET}")

def boucle_nitro_multithread():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            futures = []
            for _ in range(10):
                api_url, lien_affiche = generer_lien_nitro()
                futures.append(executor.submit(verifier_nitro, api_url, lien_affiche))
            concurrent.futures.wait(futures)

boucle_nitro_multithread()
