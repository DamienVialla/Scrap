import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time

date = datetime.date.today()
start = time.time()

for i in range(1,90):
    url = f"https://ocarat.com/recherche?id_search=1&search=montre+automatique&p={i}"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    annonces = soup.find_all("div", {"class":"product-container"})
    dico = {}
    dico1 = "#".join(["Date", "Marque","Descritpion","Prix","Solde ?"])
    with open(f"{date}-donnéesocarat.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico1)}\n")

    for i in annonces:
        try:
            prix = i.find("span", {"class":"price product-price"}).get_text()
        except:
            prix = "no price"
        
        try:
            Ancien_prix = i.find("span", {"class":"old-price product-price"}).get_text()
        except:
            Ancien_prix = "Montre pas en solde"
        #Permettrait d'avoir le pourcentage de reduc en auto mais impossible de convertire le prix en numérique
        """
        if Ancien_prix != "Montre pas en solde" and prix != "no price":
            Pourcentage_reduction = (int(Ancien_prix.strip())-int(prix.strip()))/int(Ancien_prix.strip())
        else :
            Pourcentage_reduction = "Pas de solde"
        """
        marque = i.find("span", {"class":"product-brand"}).get_text()
        designation = i.find("h3", {"class":"product-name"}).get_text()

        dico = "#".join([str(date), marque.strip(), designation.strip(),prix.strip(),Ancien_prix.strip()])

        with open(f"{date}-donnéesocarat.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico)}\n")
              
end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {int(elapsed)} s')