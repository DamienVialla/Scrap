import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import os

date = datetime.date.today()
start = time.time()

if os.path.exists(f"{date}-donnéeschrono24.csv"):
    os.remove(f"{date}-donnéeschrono24.csv")
else:
    dico1 = "§".join(["Date", "Marque","Descritpion","Prix","frais de port","Pays"])
    with open(f"{date}-donnéeschrono24.csv","a",encoding="utf-8") as fichier_extract:
        fichier_extract.write(f"{str(dico1)}\n")

for i in range(1,20):
    url = f"https://www.chrono24.fr/search/index.htm?accessoryTypes=&dosearch=true&query=montre&searchexplain=true&showpage={i}&sortorder=11&watchTypes=U"
    html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
    soup = BeautifulSoup(html.content, 'html.parser')
    annonces_texte = soup.find_all("div", {"class":"d-flex justify-content-between align-items-end m-b-1"})
    annonces_marque = soup.find_all("div", {"class":"p-x-2 p-x-sm-0"})
    dico = {}
    
    j=""

    for i,j in zip(annonces_texte, annonces_marque):
        try:
            prix = i.find("div", {"class":"text-bold"}).get_text()
        except:
            prix = "no price"
        
        try:
            frais_port = i.find("div", {"class":"text-muted text-sm"}).get_text()
        except:
            frais_port = "Montre pas en solde"
        
        marque = j.find("div", {"class":"text-bold text-ellipsis"}).get_text()
        description = j.find("div", {"class":"text-ellipsis m-b-2"}).get_text()
        pays = i.find("span", {"class":"text-sm text-uppercase"}).get_text()

        dico = "§".join([str(date),marque.strip(),description.strip(),prix.strip(),frais_port.strip(),pays.strip()])

        with open(f"{date}-donnéeschrono24.csv","a",encoding="utf-8") as fichier_extract:
            fichier_extract.write(f"{str(dico)}\n")

end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {int(elapsed)} s')