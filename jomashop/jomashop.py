#!/usr/bin/env python3
# coding: utf-8
 
import requests
from bs4 import BeautifulSoup
import datetime
import time
import os
import time
import random

#permet de savoir combien de temps dure l'execution
date = datetime.date.today()
start = time.time()

#efface le fichier portant le même nom pour en faire un nouveau
if os.path.exists(f"{date}-jomashop.csv"):
    os.remove(f"{date}-jomashop.csv")

#met les titres de colonne dans le fichier csv qui est variable avec fstring sur la date
#encodage en utf-8-sig qui marche bien, pourquoi ?
dico = "§".join(
	(
		"Date",
		"Marque",
		"Descritpion",
		"Prix",
		"reduction"
	)
)
with open(f"{date}-jomashop.csv", "w",encoding="utf-8-sig") as fichier_extract:
	print(dico, file=fichier_extract)
 
#je boucle sur l'ensemble des pages.
#test pour savoir si annonces_texte est plein ou pas pour savoir si il y a encore des pages

page=0

while True:
	actual_time = time.time()
	print("page={}".format(page)+" - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://www.jomashop.com/watches.html?p={}".format(page)
	html = requests.get(url, headers={'User-Agent': 'NokiaE70-1/3.0 (1.0610.05.06) SymbianOS/9.1 Series60/3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	#différentes annonces car toutes les infos ne se trouvent pas dans la même "div class"
	annonces_texte = soup.find_all("li", {"class":"productItem)"})
 
	# Fin de site ou limite
	if page > 5: break
	
	#simule du temps entre les scrap pour piéger le site ... Ne marche pas
	#time.sleep(random.randint(1, 4))
	
	annonces_prix = soup.find_all("div", {"class":"productPrice"})
	print (annonces_prix)
	print (annonces_texte)

	for (i, j) in zip(annonces_texte, annonces_prix): 
        
		try:
			prix = j.find("div", {"class":"price"}).get_text()
		except AttributeError:
			prix = "no price"
 
		try:
			description = i.find("a", {"title":""}).get_text()
		except AttributeError:
			description = ""
	     

		try:
			reduction = i.find("span", {"class":"discount-value show-red"}).get_text()
		except AttributeError:
			reduction = "Pas de frais de reduction"
		
		marque = i.find("span", {"class":"brand-name"}).get_text()		
		
        #mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				marque.strip(),
				description.strip(),
				prix.strip(),
				reduction.strip()
			)
		)

		# \n pour passage à la ligne
		with open(f"{date}-jomashop.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	page+=1
# while
 
# indique fin du temps pour durée d'execution
end = time.time()
print("Temps d'exécution : {}s".format(end - start))
