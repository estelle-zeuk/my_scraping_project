import requests
from bs4 import BeautifulSoup
import csv

#requette https pour récupérer la page à scraper et impression du statut de la réponse
res = requests.get('https://asso.shop/categorie-produit/smartphone/')
print(res.status_code)

#on récupère la page et on stocke le contenu après l'avoir parser
page = requests.get('https://asso.shop/categorie-produit/smartphone/')
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
print(title)

#on crée une liste qui contiendra les éléments scrapés
liste_telephone = []

#on sélectionne les éléments div avec pour class product-inner, balises dans lesquelles sont définis les téléphones
telephones = soup.select('div.product-inner')

#on itère sur ces éléments sélectionnés et on rempli la liste, chaque élément de la liste étant un dictionnaire
for telephone in telephones:
    nom_telephone = telephone.select('li.title')[0].text
    prix_telephone = telephone.select('span.woocommerce-Price-amount.amount > bdi')[0].text
    info = {
        "nom": nom_telephone.strip(),
        "prix": prix_telephone.strip()
    }
    liste_telephone.append(info)
print(liste_telephone)

#on crée un fichier csv dans lequel on écrit chacun des éléments de notre liste
fichier = open("test_phone_asso.csv", "w")
writer = csv.writer(fichier, delimiter=',')
for line in liste_telephone:
    writer.writerow(line)

