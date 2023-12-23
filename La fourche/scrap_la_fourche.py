import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time


start = time.time()

"""
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
liste_url =["sante-bio","epicerie-salee-bio","epicerie-sucree-bio","vras-bio","boissons-bio","maison-ecologique","beaute-hygiene-bio","bebe-bio-ecologique"]

for i in range(1,3):
    url = f"https://lafourche.fr/collections/anti-gaspi-1?trackingId=menu&page=1{i}"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    date = datetime.date.today()
    product_datasheet = soup.find_all("li", {"class":"jsx-6ab6887c3cf49340 card"}) 
    dico = {}
    dico1 = "#".join(["Date","Description","Marque","quantité","prix actuel","prix avant reduc","pourcentage reduc","prix par unité"])
    with open(f"{date}-données_la_fourche.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico1)}\n")

    for i in product_datasheet:
        description = i.find("span", {"class":"jsx-3927393017"}).get_text()
        marque = i.find("span", {"class":"jsx-3927393017 vendor"}).get_text()
        prix_unite = i.find("span", {"class":"jsx-3927393017 price-by-unit"}).get_text()
        prix = i.find("span", {"class":"jsx-3927393017 price"}).get_text()
        prix_avant_reduc = i.find("span", {"class":"jsx-3927393017 compared-price"}).get_text()
        pourcentage_reduc = i.find("div", {"class":"jsx-3927393017 discount-price"}).get_text()
        
        try:
             quantite = i.find("span", {"class":"jsx-3927393017 weight"}).get_text()
        except:
             quantite = "Pas de quantité"

        dico = "#".join([str(date),description.strip(),marque.strip(),quantite.strip(),prix.strip(),prix_avant_reduc.strip(),pourcentage_reduc.strip(),prix_unite.strip()])
             
        with open(f"{date}-données_la_fourche.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico)}\n")

end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {int(elapsed)} s')
