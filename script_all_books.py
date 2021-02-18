import requests
from bs4 import BeautifulSoup
import script_urls_book as SUB
import os
import time


def url_categorys(soupe):
    """ get the url of the categories"""

    urls_cats_list = []
    urls_links = soupe.find("ul", {"class": "nav-list"})
    urls_link = urls_links.findAll("a")
    for link in urls_link:
        href = f"http://books.toscrape.com/{link.get('href')}"
        urls_cats_list.append(href)
    return urls_cats_list[1:51]


def main():
    """general function of the script"""

    url_site = "https://books.toscrape.com/"
    try:
        page_book = requests.get(url_site)
    except requests.exceptions.RequestException as e:
        print(
            "Probleme de connection, veuillez vérifier votre connection internet ou rentrer un url valide"
        )
        raise SystemExit(e)
    soupe = BeautifulSoup(page_book.content, "html.parser")
    categories_urls = url_categorys(soupe)
    all_books_list = []
    for urls in categories_urls:
        all_data = SUB.get_all_books_for_one_category(urls)
        for books in all_data:
            all_books_list.append(books)

    return


if __name__ == "__main__":

    directory_name = "Book_Scraping"
    print("Le script est lancé, le nom de dossier sera par défaut Book_Scraping")
    time.sleep(5)
    try:
        os.mkdir(directory_name)
        print(f"Votre dossier : {directory_name} à été crée")
    except:
        print(
            f"Votre dossier : {directory_name} est déjà existant,le script va remplacer les données existantes du dossier"
        )
    finally:
        os.chdir(directory_name)
    time.sleep(5)
    print(f"Les données sont en cours de sauvgarde dans votre dossier {directory_name}")
    time.sleep(2)
    print("Merci de patienter pendant l'execution du script")
    main()
    print(
        f"Le script viens de finir, vous pouvez retrouver vos données dans votre dossier {directory_name}"
    )