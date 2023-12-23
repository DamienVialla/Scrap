#!/usr/bin/env python3
# coding: utf-8
 
import requests
from bs4 import BeautifulSoup
import datetime
import time
import os

#permet de savoir combien de temps dure l'execution
date = datetime.date.today()
start = time.time()

#efface le fichier portant le même nom pour en faire un nouveau
if os.path.exists(f"{date}-donnéeschrono24.csv"):
    os.remove(f"{date}-donnéeschrono24.csv")

#met les titres de colonne dans le fichier csv qui est variable avec fstring sur la date
#encodage en utf-8-sig qui marche bien, pourquoi ?
dico = "§".join(
	(
		"Date",
		"Vrai Marque",
		"Marque",
		"Descritpion",
		"Prix",
		"frais de port",
		"Pays",
	)
)
with open(f"{date}-donnéeschrono24.csv", "w",encoding="utf-8-sig") as fichier_extract:
	print(dico, file=fichier_extract)
 
#je boucle sur l'ensemble des pages.
#test pour savoir si annonces_texte est plein ou pas pour savoir si il y a encore des pages

page=0

while True:
	actual_time = time.time()
	print("page={}".format(page)+" - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://www.chrono24.fr/search/index.htm?accessoryTypes=&dosearch=true&query=montre&searchexplain=true&showpage={}&sortorder=11&watchTypes=U".format(page)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	print(url)
	#différentes annonces car toutes les infos ne se trouvent pas dans la même "div class"
	annonces_texte = soup.find_all("div", {"class":"d-flex justify-content-between align-items-end m-b-1"})
 
	# Fin de site ou limite
	if not annonces_texte or page > 50: break
 
	annonces_marque = soup.find_all("div", {"class":"p-x-2 p-x-sm-0"})
	annonces_vrai_marque = soup.find_all("div", {"class":"article-item-container wt-search-result carousel-test"})
 
	for (i, j, k) in zip(annonces_texte, annonces_marque, annonces_vrai_marque): 
        
		try:
			prix = i.find("div", {"class":"text-bold"}).get_text()
		except AttributeError:
			prix = "no price"
 
		try:
			description = j.find("div", {"class":"text-ellipsis m-b-2"}).get_text()
		except AttributeError:
			description = ""
	     

		try:
			frais_port = i.find("div", {"class":"text-muted text-sm"}).get_text()
		except AttributeError:
			frais_port = "Pas de frais de port"
		
		marque_generique = k.find("a", {"data-manufacturer"})
		marque = j.find("div", {"class":"text-bold text-ellipsis"}).get_text()
		description = j.find("div", {"class":"text-ellipsis m-b-2"}).get_text()
		pays = i.find("span", {"class":"text-sm text-uppercase"}).get_text()
		
		
        #mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				str(marque_generique),
				marque.strip(),
				description.strip(),
				prix.strip(),
				frais_port.strip(),
				pays.strip(),
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéeschrono24.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	page+=1
# while
 
# indique fin du temps pour durée d'execution
end = time.time()
print("Temps d'exécution : {}s".format(end - start))