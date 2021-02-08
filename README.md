# OC-QL-Projet-02

Pour ce projet 2, il est demandé de récupérer sur le site http://books.toscrape.com/ les informations ci-dessus pour chaque livres de chaque catégories: 

- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

Chacune des informations des livres pour chaque catégories seront enregistrer dans un fichier .csv, leur images seront téléchargées et stockées en local sur l'ordinateur.

Procédure d’exécution du script :

1.Installation de GIT
Si GIT n'est pas installé sur votre machine, 
téléchargé et installé le : https://git-scm.com/downloads

2.Clonage du répertoire
Crée un dossier et initialisé votre dépôt local
tapez : git init 

tapez: git clone https://github.com/quentin8469/OC-QL-Projet-02.git

3.Création et activation de l'environnement virtuel
Dans la console de votre choix tapez : 
python -m venv env 

Pour l'activer :
Sous Windows : venv/scripts/activate
Sous Linux : env/bin/activate

4.Installation des librairies

Pour installer les librairies depuis le fichier 'requirements.txt'
Via la console tapez :
pip install -r requirements.txt

Pour exécuter le programme, il vous faudra dans taper la commande qui suit dans votre terminal :

python « nomduprojet.py »

Le script va créer un dossier dans lequel vous retrouverez les .csv de chaque catégories ainsi que toutes les images des livres.
