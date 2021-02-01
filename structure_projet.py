import requests
from bs4 import BeautifulSoup

def get_product_page_url(url_du_livre):
    """ recuper l'url de la page du livre """
    
    book_url = url_du_livre
    
    return book_url


def get_universal_product_code(soupe):
    """ doc """
    upc = soupe.find_all('td')[0].text
    
    return upc


def get_title(soupe):
    """ doc """
    
    title = soupe.find('h1').text
    
    return title


def get_price_including_tax(soupe):
    """ doc """
    
    price_including_tax = soupe.find_all('td')[3].text
    return price_including_tax


def get_price_excluding_tax(soupe):
    """ doc """
    price_excluding_tax = soupe.find_all('td')[2].text
    return price_excluding_tax


def get_tax(soupe):
    """ doc """
    tax = soupe.find_all('td')[4].text
    return tax


def get_number_available(soupe):
    """ doc """
    number_available = soupe.find_all('td')[5].text
    return number_available


def get_product_description(soupe):
    """ doc """
    product_description = soupe.find_all('p')[3].text
    return product_description


def get_category(soupe):
    """ doc """
    category = soupe.find_all('li')[2].text.strip()
    return category


def get_review_rating(soupe):
    """ doc """
    review_rating = soupe.find_all('td')[6].text
    
    return review_rating


def get_image_url(soupe):
    """ doc """
    
    image_book = soupe.find('img').get('src')
    url_image = image_book.replace('../../',
                                   'http://books.toscrape.com/')
    return url_image

def get_data_in_dictionnarie():
    """ doc """
    url_du_livre = 'https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
    html = requests.get(url_du_livre)
    soupe = BeautifulSoup(html.content, 'html.parser')
    
    book_data = {}
    
    book_data['Book_Url'] = get_product_page_url(url)
    book_data['Category'] = get_category(soupe)
    book_data['Titles'] = get_title(soupe)
    book_data['Description'] = get_product_description(soupe)
    book_data['UPC'] = get_universal_product_code(soupe)
    book_data['Price_including_tax'] = get_price_including_tax(soupe)
    book_data['Price_excluding_tax'] = get_price_excluding_tax(soupe)
    book_data['Tax '] = get_tax(soupe)
    book_data['Number_available'] = get_number_available(soupe)
    book_data['Review_rating'] = get_review_rating(soupe)
    book_data['Image_url'] = get_image_url(soupe)
    
    return book_data






def recuperer_les_informations_pour_un_livre(url_d_un_livre):
    """ fonction qui stockera les informations d'un livre dans un dictionnaire
    besoin de l'url d'un livre """
    
    dictionnaire_des_information_du_livre = {"titre" : "nom du livre", 
                                              "upc" : "09747478",
                                        "categorie" : "action"}
    print('extraction des données du livre_dans_un_dictionnaire')
    return dictionnaire_des_information_du_livre


def recuperer_tout_les_livres_pour_une_categories(liste_des_urls_de_tous_les_livres_de_la_categorie):
    """ fonction qui recupera une liste de dictionnaires avec toutes les inforamtions de chaques livres
    et fournie l'url du livre à la fonction recuperer_les_informations_pour_un_livre """
    
    liste_de_dictionnaires_des_inforamtions_de_tout_les_livres_dune_page = [{"titre" : "nom du livre", 
                                              "upc" : "09747478",
                                        "categorie" : "action"}, {"titre" : "nom du livre", 
                                              "upc" : "09747478",
                                        "categorie" : "action"}]
    #envoie les urls des livres d'une categorie les uns apres les autres
    for url_d_un_livre in liste_des_urls_de_tous_les_livres_de_la_categorie:
        toutes_les_infos_des_livres_d_une_page = recuperer_les_informations_pour_un_livre(url_d_un_livre)
        # boucle qui remplie la liste avec les dictionnaire de data de chaque livres de la categorie
        for informations_livre in toutes_les_infos_des_livres_d_une_page:
            liste_de_dictionnaires_des_inforamtions_de_tout_les_livres_dune_page.append(informations_livre)
    print('extration des dictionnaires de tout les livres de la categories')
    return liste_de_dictionnaires_des_inforamtions_de_tout_les_livres_dune_page


def recuperer_toutes_les_urls_des_livres_de_la_categories(urls_des_pages):
    """ fonction qui recupere les urls de chaques livres d'une categorie pour fournir la liste à la
    fonction recuperer_tout_les_livres_pour_une_categories. Recupere une liste de dictionnaire de tout 
    les livres de chaques categories """
    
    # liste de toutes les urls des livres par categories utilisées pour recuperer les urls des livres
    liste_des_urls_de_tous_les_livres_de_la_categorie = ['http//livre01', 'http//livre02', 'http//livre03']
    # liste de liste de dictionnaire 
    liste_de_liste_de_dictionnaire_des_livres_de_chaques_categories =[[{}], [{}]]

    liste_de_dictionnaire_des_livres = recuperer_tout_les_livres_pour_une_categories(liste_des_urls_de_tous_les_livres_de_la_categorie)
    # boucle pour créer la liste_de_liste_de_dictionnaire_des_livres_de_chaque_categories
    for dictionnaires_de_livres in liste_de_dictionnaire_des_livres:
        liste_de_liste_de_dictionnaire_des_livres_de_chaques_categories.append(dictionnaires_de_livres)
    
    print('liste avec tout les livres')
    return liste_de_liste_de_dictionnaire_des_livres_de_chaques_categories


def recuperer_toutes_les_pages_des_categories(liste_de_toutes_les_urls_des_categories):
    """ fonction qui verifie si il a y plusieurs page dans l'url de chaque categorie """
    
    liste_des_pages_de_chaques_categories = ['http//categorie-page1', 'http//categorie-page2']
    variable = recuperer_toutes_les_urls_des_livres_de_la_categories(liste_des_pages_de_chaques_categories)
    print('urls des pages pour toutes les categories')
    return liste_des_pages_de_chaques_categories


def recuperer_toutes_les_urls_des_categories(url_du_site):
    """ fonction qui permettra d'extraire les urls de toute les categories du site """
    

    liste_de_toutes_les_urls_des_categories = ['http//categorie01', 'http//categorie02', 'http//categorie03']
    liste_des_pages_de_chaques_categories = ['http//categorie-page1', 'http//categorie-page2']
    # resquests avec url_du_site
    # beautifullsoup pour recuperer et stocker les urls dans la liste
    toute_les_urls_des_categories = recuperer_toutes_les_pages_des_categories(liste_de_toutes_les_urls_des_categories)
    for pages_categories in toute_les_urls_des_categories:
        toutes_les_urls_des_pages_de_chaques_categories = recuperer_toutes_les_pages_des_categories(pages_categories)
        for listes_des_urls_des_pages in toutes_les_urls_des_pages_de_chaques_categories:
            liste_des_pages_de_chaques_categories.append(listes_des_urls_des_pages)

    print('urls des categories')
    return liste_des_pages_de_chaques_categories

def main():
    """ fonction principale pour l'execution du script"""
    
    url_du_site = 'https://books.toscrape.com/'
    
    
    toutes_les_urls_des_pages_de_chaque_categories = recuperer_toutes_les_urls_des_categories(url_du_site)
    
    
    liste_dictionnaires_de_tout_les_livres_de_chaque_categories = [] # liste de dictionnaire à sauvgerder au format csv
    #boucle pour stocker les info dans liste_dictionnaires_de_tout_les_livres_de_chaque_categories
    for urls_des_pages in toutes_les_urls_des_pages_de_chaque_categories:
        all_books_data = recuperer_toutes_les_urls_des_livres_de_la_categories(urls_des_pages)
        for informations_du_livre in all_books_data:
            liste_dictionnaires_de_tout_les_livres_de_chaque_categories.append(informations_du_livre)
    print('scrap de tout ')
			
if __name__ == '__main__':
    main()
