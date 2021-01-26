

def recuperer_les_informations_pour_un_livre(url_d_un_livre):
    """ fonction qui stockera les informations d'un livre dans un dictionnaire """
    
    dictionnaire_des_information_du_livre = {"titre" : "nom du livre", 
                                              "upc" : "09747478",
                                        "categorie" : "action"}
    print('extraction des données du livre')
    return dictionnaire_des_information_du_livre


def recuperer_tout_les_livres_pour_une_categories(liste_des_urls_de_tous_les_livres_de_la_categorie):
    """ fonction qui recupera une liste de dictionnaires avec toutes les inforamtions de chaques livres """
    
    liste_de_dictionnaire_des_inforamtions_de_tout_les_livres_dune_page = [{"titre" : "nom du livre", 
                                              "upc" : "09747478",
                                        "categorie" : "action"}, {"titre" : "nom du livre", 
                                              "upc" : "09747478",
                                        "categorie" : "action"}]
    for url_d_un_livre in liste_des_urls_de_tous_les_livres_de_la_categorie:
        toutes_les_infos_des_livres_d_une_page = recuperer_les_informations_pour_un_livre(url_d_un_livre)

        for informations_livre in toutes_les_infos_des_livres_d_une_page:
            liste_de_dictionnaire_des_inforamtions_de_tout_les_livres_dune_page.append(informations_livre)
    print('extration des dictionnaires')
    return liste_de_dictionnaire_des_inforamtions_de_tout_les_livres_dune_page


def recuperer_toutes_les_urls_des_livres_de_la_categories(liste_des_pages_de_chaques_categories):
    """ fonction qui recupera les urls de chaques livres d'un categorie """
    
    liste_des_urls_de_tous_les_livres_de_la_categorie = ['http//livre01', 'http//livre02', 'http//livre03']
    liste_de_liste_de_dictionnaire_des_livres_de_chaque_categories =[[{}], [{}]]
    liste_de_dictionnaire_des_livres = recuperer_tout_les_livres_pour_une_categories(liste_des_urls_de_tous_les_livres_de_la_categorie)
    for dictionnaires_de_livres in liste_de_dictionnaire_des_livres:
        liste_de_liste_de_dictionnaire_des_livres_de_chaque_categories.append(dictionnaires_de_livres)
    print('liste des urls des livres')
    print('liste avec tout les livres')
    return liste_des_urls_de_tous_les_livres_de_la_categorie


def recuperer_toutes_les_pages_des_categories(liste_de_toutes_les_urls_des_categories):
    """ fonction qui verifiera si il a y plusieurs page dans l'url de chaque categorie """
    
    liste_des_pages_de_chaques_categories = ['http//categorie-page1', 'http//categorie-page2']
    variable = recuperer_toutes_les_urls_des_livres_de_la_categories(liste_des_pages_de_chaques_categories)
    print('urls des pages pour une categories')
    return liste_des_pages_de_chaques_categories


def recuperer_toutes_les_urls_des_categories(url_du_site):
    """ fonction qui permettra d'extraire les urls de toute les categories du site """
    

    liste_de_toutes_les_urls_des_categories = ['http//categorie01', 'http//categorie02', 'http//categorie03']
    # resquests avec url_du_site
    # beautifullsoup pour recuperer et stocker les urls dans la liste
    variable = recuperer_toutes_les_pages_des_categories(liste_de_toutes_les_urls_des_categories)
    
    return liste_de_toutes_les_urls_des_categories

def main():
    """ fonction principale pour l'execution du script"""
    
    url_du_site = 'https://books.toscrape.com/'
    
    
    tous_les_livres_de_chaque_categories = recuperer_toutes_les_urls_des_categories(url_du_site)
    
    #boucle pour stocker les info dans liste_dictionnaires_de_tout_les_livres_de_chaque_categories
    liste_dictionnaires_de_tout_les_livres_de_chaque_categories = [] # liste de dictionnaire à sauvgerder au format csv
    
    for informations_des_livres in tous_les_livres_de_chaque_categories:
        for informations_du_livre in informations_des_livres:
            liste_dictionnaires_de_tout_les_livres_de_chaque_categories.append(informations_du_livre)
			

if __name__ == '__main__':
    main()
