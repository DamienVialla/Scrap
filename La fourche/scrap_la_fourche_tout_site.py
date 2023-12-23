import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time


start = time.time()

"""
url des différentes catégorie lafourche et code pour parser
https://lafourche.fr/collections/boissons-alcoolisees?trackingId=menu   <div class="jsx-3927393017 container-price">
https://lafourche.fr/collections/anti-gaspi-1?trackingId=menu   <div class="jsx-3927393017 container">
https://lafourche.fr/collections/sante-bio?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/epicerie-salee-bio?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/epicerie-sucree-bio?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/vrac-bio?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/boissons-bio?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/maison-ecologique?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/beaute-hygiene-bio?trackingId=menu   <div class="jsx-2564600132 container-price">
https://lafourche.fr/collections/bebe-bio-ecologique?trackingId=menu   <div class="jsx-2564600132 container-price">
"""

liste_url =["sante-bio","epicerie-salee-bio","epicerie-sucree-bio","vrac-bio","boissons-bio","maison-ecologique","beaute-hygiene-bio","bebe-bio-ecologique"]
date = datetime.date.today()
dico1 = "#".join(["Date","Categorie","Description","Marque","quantité","prix actuel","prix avant reduc","pourcentage reduc","prix par unité"])
with open(f"{date}-données_la_fourche.csv","a") as fichier_extract:
    fichier_extract.write(f"{str(dico1)}\n")

for j in liste_url:
    for i in range(1,3):
        url = f"https://lafourche.fr/collections/{j}?trackingId=menu&page={i}"
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        product_datasheet = soup.find_all("li", {"class":"jsx-6ab6887c3cf49340 card"}) 
        dico = {}
        for i in product_datasheet:
            try:
                description = i.find("span", {"class":"jsx-2564600132"}).get_text()
            except:
                description = "aucune"
            
            try :    
                marque = i.find("span", {"class":"jsx-2564600132 vendor"}).get_text()
            except:
                marque = "aucune"
            
            try :
                prix_unite = i.find("span", {"class":"jsx-2564600132 price-by-unit"}).get_text()
            except :
                prix_unite = "aucun"
            
            try:
                prix = i.find("span", {"class":"jsx-2564600132 price"}).get_text()
            except:
                prix = "aucun"
            
            try:
                prix_avant_reduc = i.find("span", {"class":"jsx-2564600132 compared-price"}).get_text()
            except:
                prix_avant_reduc = "aucun"
            
            try:
                pourcentage_reduc = i.find("div", {"class":"jsx-2564600132 discount-price"}).get_text()
            except:
                pourcentage_reduc = "aucun"
        
            try:
                quantite = i.find("span", {"class":"jsx-2564600132 weight"}).get_text()
            except:
                quantite = "Pas de quantité"

            dico = "#".join([str(date),j,description.strip(),marque.strip(),quantite.strip(),prix.strip(),prix_avant_reduc.strip(),pourcentage_reduc.strip(),prix_unite.strip()])
             
            with open(f"{date}-données_la_fourche.csv","a",encoding="utf-16") as fichier_extract:
                fichier_extract.write(f"{str(dico)}\n")
            
            #print(quantite)
            #print(pourcentage_reduc)
            #print(prix_avant_reduc)
            #print(prix)
            #print(prix_unite)
            #print(marque)
            #print(description)
    
end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {int(elapsed)} s')
