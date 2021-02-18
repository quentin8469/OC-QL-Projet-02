import requests
from bs4 import BeautifulSoup
import script_write_datas as SWD
import Script_data_book as SDB


def check_number_pages(url_actuelle):
    """ check if we have a have. if href we have other page """

    html = requests.get(url_actuelle)
    soupe = BeautifulSoup(html.content, "html.parser")
    check_url = soupe.find("li", {"class": "next"})
    if check_url != None:
        check_url = soupe.find("li", {"class": "next"}).select("a")
        href = check_url[0]["href"]
        return href
    return None


def get_all_page(url_one_categorie):
    """ make a list of all page in one categories """

    liste_all_pages = []
    liste_all_pages.append(url_one_categorie)
    check_href = check_number_pages(url_one_categorie)
    if check_href != None:
        url_de_base = url_one_categorie.rsplit("/", 1)
        page_url = url_de_base[0] + str("/" + check_href)
        other_page = get_all_page(page_url)
        for page in other_page:
            liste_all_pages.append(page)
    return liste_all_pages


def urls_books_categorys(url_page):
    """ get the books urls in one category"""
    urls_books_list = []
    page_book = requests.get(url_page)
    soupe = BeautifulSoup(page_book.content, "html.parser")
    books = soupe.select(".product_pod")
    for book in books:
        titles = book.select("a")[1]["href"]
        title = titles.replace("../../../", "http://books.toscrape.com/catalogue/")
        urls_books_list.append(title)
    return urls_books_list


def get_all_books_for_one_category(urls):
    """make a list of all url book for one categorie, get a list of dictionnarie
    of all books in one category"""

    urls_liste_pages = []
    infos_books_list = []
    url_one_categorie = urls
    urls_categories_pages = get_all_page(url_one_categorie)
    for url_page in urls_categories_pages:
        urls_books = urls_books_categorys(url_page)
        for urls in urls_books:
            urls_liste_pages.append(urls)
    for url_books in urls_liste_pages:
        infos_data = SDB.get_data_in_dictionnarie(url_books)
        infos_books_list.append(infos_data)
    SWD.write_books_data(infos_books_list)
    return infos_books_list


if __name__ == "__main__":
    get_all_books_for_one_category()