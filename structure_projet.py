

def recuperer_les_informations_pour_un_livre():
    """ """
    
    dictionnaire_des_information_du_livre = {}
    
    return dictionnaire_des_information_du_livre



def recuperer_tout_les_livres_pour_une_categories():
    """ """
    
    liste_de_dictionnaire_des_inforamtions_de_tout_les_livres_d'une_page = [{}]
    
    return liste_de_dictionnaire_des_inforamtions_de_tout_les_livres_d'une_page


def recuperer_toutes_les_urls_des_livres_de_la_categories():
    """ """
    
    liste_des_urls_de_tous_les_livres_de_la_categorie = []
    
    
    return liste_des_urls_de_tous_les_livres_de_la_categorie


def recuperer_toutes_les_pages_des_categories():
    """ """
    
    liste_des_pages_de_chaques_categories = []
    
    
    return liste_des_pages_de_chaques_categories



def recuperer_toutes_les_urls_des_categories(url_du_site):
    """ fonction qui permettra d'extraire les url de toute les categories du site """
    
    liste_de_toutes_les_urls_des_categories = []

    
    return liste_de_toutes_les_urls_des_categories

def main():
    """ fonction principale pour l'execution du script"""
    
    url_du_site = 'https://books.toscrape.com/'
    
    
    tous_les_livres_de chaque_categories = recuperer_toutes_les_urls_des_categories(url_du_site)
    
    #boucle pour stocker les info dans liste_dictionnaires_de_tout_les_livres_de_chaque_categories
    liste_dictionnaires_de_tout_les_livres_de_chaque_categories =[] # liste de dictionnaire à sauvgerder au format csv
    
    for informations_des_livres in tous_les_livres_de chaque_categories:
        for informations_du_livre in informations_des_livres:
            liste_de_tout_les_livres_de_chaque_categories.append(informations_du_livre)