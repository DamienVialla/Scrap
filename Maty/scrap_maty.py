import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time

date = datetime.date.today()
start = time.time()

for i in range(1,4):
    url = f"https://www.maty.com/montres-automatiques.html/I-Page{i}_36"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    annonces = soup.find_all("div", {"class":"fav-wrapper"})
    dico = {}
    dico1 = "#".join(["Date", "Marque","Descritpion","Prix","Solde ?"])
    with open(f"{date}-donnéesmaty.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico1)}\n")
    print(url)
    print(annonces)

    for i in annonces:
        try:
            prix = i.find("div", {"class":"prix-base"}).get_text()
        except:
            prix = "no price"
        
        try:
            frais_port = i.find("div", {"class":"prix-bar"}).get_text()
        except:
            frais_port = "Montre pas en solde"
        
        designation = i.find("h2", {"class":"desc"}).get_text() 
        marque = i.find("p", {"class":"titre"}).get_text()

        dico = "#".join([str(date), designation.strip(),prix.strip(),frais_port.strip()])

        with open(f"{date}-donnéesmaty.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico)}\n")
              
end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {int(elapsed)} s')