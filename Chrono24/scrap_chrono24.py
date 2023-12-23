import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time

date = datetime.date.today()
start = time.time()

for i in range(1,4):
    url = f"https://www.chrono24.fr/search/index.htm?accessoryTypes=&dosearch=true&query=montre&searchexplain=1&showpage={i}&watchTypes="
    html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
    soup = BeautifulSoup(html.content, 'html.parser')
    annonces = soup.find_all("div", {"class":"d-flex justify-content-between align-items-end m-b-1"})
    dico = {}
    dico1 = "#".join(["Date", "Marque","Descritpion","Prix","Solde ?"])
    #with open(f"{date}-donnéeschrono24.csv","a") as fichier_extract:
    #        fichier_extract.write(f"{str(dico1)}\n")
   
    for i in annonces:
        try:
            prix = i.find("div", {"class":"text-bold"}).get_text()
        except:
            prix = "no price"
        
        try:
            frais_port = i.find("div", {"class":"text-muted text-sm"}).get_text()
        except:
            frais_port = "Montre pas en solde"
        
        #marque = i.find("div", {"class":"text-bold text-ellipsis"}).get_text() 
        #description = i.find("p", {"div":"text-ellipsis m-b-2"}).get_text()
        pays = i.find("span", {"class":"text-sm text-uppercase"}).get_text()

        dico = "#".join([str(date),prix.strip(),frais_port.strip(),pays.strip()])

        with open(f"{date}-donnéeschrono24.csv","a",encoding="UTF-16") as fichier_extract:
            fichier_extract.write(f"{str(dico)}\n")

end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {int(elapsed)} s')