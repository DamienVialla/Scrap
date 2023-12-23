#!/usr/bin/env python3
# coding: utf-8
 
import requests
from bs4 import BeautifulSoup
import datetime
import time
import os
import re
import module_damien

#permet de savoir combien de temps dure l'execution
date = datetime.date.today()
start = time.time()

#efface le fichier portant le même nom pour en faire un nouveau
if os.path.exists(f"{date}-donnéesglobal.csv"):
    os.remove(f"{date}-donnéesglobal.csv")

#met les titres de colonne dans le fichier csv qui est variable avec fstring sur la date
#encodage en utf-8-sig qui marche bien, pourquoi ?
dico = "§".join(
	(
		"Date",
		"Site", 
		"Marque",
		"Descritpion",
		"Prix",
		"Ancien Prix"
	)
)
with open(f"{date}-donnéesglobal.csv", "w",encoding="utf-8-sig") as fichier_extract:
	print(dico, file=fichier_extract)
 

page_ocarat=1
page_louispion=1
page_maty=1
pages_timeshop24=1
pages_conteenium=1
pages_fiyta=1

while True:

	actual_time = time.time()
	print("page={}".format(page_ocarat)+" - Ocarat - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://ocarat.com/recherche?id_search=1&search=montre+automatique&p={}".format(page_ocarat)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	annonces_ocarat = soup.find_all("div", {"class":"product-container"})
	
	# Fin de site ou limite
	if not annonces_ocarat or page_ocarat > 500: 
		break

	for i in annonces_ocarat :
		
		try:
			prix = i.find("span", {"class":"price product-price"}).get_text()
		except:
			prix = "no price"
			
		try:
			Ancien_prix = i.find("span", {"class":"old-price product-price"}).get_text()
		except:
			Ancien_prix = prix
			
		marque = i.find("span", {"class":"product-brand"}).get_text()
		designation = i.find("h3", {"class":"product-name"}).get_text()

		#mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				"Ocarat",
				marque.strip(),
				designation.strip(),
				prix.strip(),
				Ancien_prix.strip(),
				#module_damien.garder_chiffre(prix),
				#module_damien.garder_chiffre(Ancien_prix)
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéesglobal.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	page_ocarat+=1
# while Ocarat

while True:

	actual_time = time.time()
	print("page={}".format(page_louispion)+" - Louis Pion - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://www.louispion.fr/montres/homme/mecanisme/automatique.html?product_list_order=saving&p={}".format(page_louispion)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	annonces_louispion = soup.find_all("div", {"class":"product details product-item-details"})
	
	# Fin de site ou limite
	if not annonces_louispion or page_louispion > 500: 
		break

	for i in annonces_louispion :
		
		try:
			prix = i.find("span", {"class":"price"}).get_text()
		except:
			prix = "no price"
			
		try:
			Ancien_prix = i.find("span", {"class":"old-price product-price"}).get_text()
		except:
			Ancien_prix = prix
			
		marque = i.find("span", {"class":"brand-label"}).get_text()
		designation = i.find("a", {"class":"product-item-link"}).get_text()

		#mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				"Louis Pion",
				marque.strip(),
				designation.strip(),
				prix.strip(),
				Ancien_prix.strip(),
				#module_damien.garder_chiffre(prix),
				#module_damien.garder_chiffre(Ancien_prix)
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéesglobal.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	page_louispion+=1
# while Louis Pion

while True:

	actual_time = time.time()
	print("page={}".format(page_maty)+" - Maty - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://www.maty.com/montres-automatiques.html/TW-10124D_1695D_10118D/I-Page{}_36".format(page_maty)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	annonces_maty = soup.find_all("div", {"class":"infos-wrapper"})
	
	# Fin de site ou limite
	if not annonces_maty or page_maty > 500: 
		break

	for i in annonces_maty :
		
		try:
			prix = i.find("p", {"class":"prix-base"}).get_text()
		except:
			prix = i.find("p", {"class":"prix-final"}).get_text()
			
		try:
			Ancien_prix = i.find("span", {"p":"old-prix-bar"}).get_text()
		except:
			Ancien_prix = prix
			
		marque = i.find("p", {"class":"titre"}).get_text()
		designation = i.find("h2", {"class":"desc"}).get_text()
		prix_travaillé = [float(s) for s in re.findall(r'-?\d+\.?\d*', prix)]
		Ancien_prix_travaillé = [float(s) for s in re.findall(r'-?\d+\.?\d*', Ancien_prix)]

		#mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				"Maty",
				marque.strip(),
				designation.strip(),
				prix.strip(),
				Ancien_prix.strip(),
				#module_damien.garder_chiffre(prix),
				#module_damien.garder_chiffre(Ancien_prix)
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéesglobal.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	page_maty+=1
# while Maty

while True:

	actual_time = time.time()
	print("page={}".format(pages_timeshop24)+" - Time Shop24 - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://www.timeshop24.fr/montres/montres-automatiques.html?p={}&product_list_order=saving".format(pages_timeshop24)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	annonces_timeshop24 = soup.find_all("div", {"class":"product details product-item-details"})
	
	# Fin de site ou limite
	if not annonces_timeshop24 or pages_timeshop24 > 500: 
		break

	for i in annonces_timeshop24 :
		
		try:
			prix = i.find("span", {"class":"final-price"}).get_text()
		except:
			prix = "no price"
			
		try:
			Ancien_prix = i.find("span", {"class":"price"}).get_text()
		except:
			Ancien_prix = prix
			
		marque = i.find("a", {"class":"product-item-link"}).get_text()
		designation = "aucune"
	
		#mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				"Time Shop24",
				marque.strip(),
				designation.strip(),
				prix.strip(),
				Ancien_prix.strip(),
				#module_damien.garder_chiffre(prix),
				#module_damien.garder_chiffre(Ancien_prix)
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéesglobal.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	pages_timeshop24+=1
# while Time Shop24

while True:

	actual_time = time.time()
	print("page={}".format(pages_conteenium)+" - conteenium - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://conteenium.fr/montre-automatique/page/{}/?yith_wcan=1&onsale_filter=1".format(pages_conteenium)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	annonces_conteenium = soup.find_all("a", {"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
	annonces_conteenium_ancien_prix = soup.find_all("del", {"aria-hidden":"true"})
	annonces_conteenium_prix = soup.find_all("ins")
	
	# Fin de site ou limite
	if not annonces_conteenium or pages_conteenium > 500: 
		break
	i=""
	j=""
	k=""
	for i,j,k in zip(annonces_conteenium,annonces_conteenium_ancien_prix,annonces_conteenium_prix) :
		
		try:
			prix = k.find("span", {"class":"woocommerce-Price-amount amount"}).get_text()
		except:
			prix = "no price"
			
		try:
			Ancien_prix = j.find("span", {"class":"woocommerce-Price-amount amount"}).get_text()
		except:
			Ancien_prix = prix
			
		marque = i.find("h2", {"class":"woocommerce-loop-product__title"}).get_text() 
		designation = "aucune"
	
		#mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				"conteenium",
				marque.strip(),
				designation.strip(),
				prix.strip(),
				Ancien_prix.strip(),
				#module_damien.garder_chiffre(prix),
				#module_damien.garder_chiffre(Ancien_prix)
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéesglobal.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	pages_conteenium+=1
# while conteenium
"""
while True:

	actual_time = time.time()
	print("page={}".format(pages_fiyta)+" - Fiyta - Temps d'exécution : {}s".format(int(actual_time - start)))
	url = "https://fiyta.fr/categorie-produit/homme/page/{}/".format(pages_fiyta)
	html = requests.get(url, headers={'User-Agent': 'Mozilla Firefox'})
	soup = BeautifulSoup(html.content, 'html.parser')
	
	annonces_fiyta = soup.find_all("div", {"class":"thb-product-inner-content"})
	annonces_fiyta_ancien_prix = soup.find_all("del", {"aria-hidden":"true"})
	annonces_fiyta_prix = soup.find_all("ins")
	
	# Fin de site ou limite
	if not annonces_fiyta or pages_fiyta > 500: 
		break

	for i,j,k in zip(annonces_fiyta, annonces_fiyta_ancien_prix,annonces_fiyta_prix) :
		
		try:
			prix = k.find("span", {"class":"woocommerce-Price-currencySymbol"}).get_text()
		except:
			prix = "no price"
			
		try:
			Ancien_prix = j.find("span", {"class":"woocommerce-Price-currencySymbol"}).get_text()
		except:
			Ancien_prix = prix
			
		designation = i.find("h2", {"class":"woocommerce-loop-product__title"}).get_text()
	
		#mets toutes les variables dans la liste. Obligé de mettre date et marque_generique en string ...
		dico = "§".join(
			(
				str(date),
				"Fiyta",
				"Fiyta",
				designation.strip(),
				prix.strip(),
				Ancien_prix.strip(),
			)
		)
 
		#toujours encoding utf-8-sig, pourquoi ?
		# \n pour passage à la ligne
		with open(f"{date}-donnéesglobal.csv", "a",encoding="utf-8-sig") as fichier_extract:
			print(dico, file=fichier_extract)
	# for
	pages_fiyta+=1
# while Fiyta
"""

# indique fin du temps pour durée d'execution
end = time.time()
print("Temps d'exécution : {}s".format(end - start))