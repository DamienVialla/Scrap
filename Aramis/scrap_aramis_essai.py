import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1,10):
    url = f"https://www.aramisauto.com/achat/recherche?page={i}"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
 
    vehicle_fiche = soup.find_all("div", {"class":"link"}) 
    dico = {}
    #with open("donnéesaramis.csv","a") as fichier_extract:
     #   fichier_extract.write(str(vehicle_fiche))

    for i in vehicle_fiche:
        try:
            kilometrage = i.find("div", {"class":"vehicle-zero-km"}).get_text()
        except:
            kilometrage = "véhicule neuf"
        motorisation = i.find("div", {"class":"vehicle-motorisation"}).get_text()
        marque = i.find("span", {"class":"vehicle-model"}).get_text()
        carburant = i.find("div", {"class":"vehicle-transmission"}).get_text()
        prix = i.find("span", {"class":"vehicle-loa-offer"}).get_text()
        dico = "#".join([marque.strip(),motorisation.strip(),kilometrage.strip(),carburant.strip(),prix.strip()])
        with open("données_aramis.csv","a") as fichier_extract:
            fichier_extract.write(f"{str(dico)}\n")

