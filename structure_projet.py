import requests
from bs4 import BeautifulSoup
import csv342 as csv


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


def telecharge_image(soupe):
    """ doc """
    titre_image = soupe.find('h1').text
    
    image_book = soupe.find('img').get('src')
    url_image = image_book.replace('../../',
                                   'http://books.toscrape.com/')
    lien_image = requests.get(url_image)
    f = open(titre_image +'.jpg','wb')
    f.write(lien_image.content)
    f.close()

 
def get_data_in_dictionnarie(url_livre):
    """ doc """
    
    url_du_livre = url_livre
    html = requests.get(url_du_livre)
    soupe = BeautifulSoup(html.content, 'html.parser')
    telecharge_image(soupe)
    book_data = {}
    
    book_data['Book_Url'] = get_product_page_url(url_du_livre)
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
   

def verifie_si_plusieurs_page(url_actuelle):
    """ doc """
    
    html = requests.get(url_actuelle)
    soupe = BeautifulSoup(html.content, 'html.parser')
    check_url = soupe.find('li', {'class': 'next'})
    if check_url != None:
        check_url = soupe.find('li', {'class': 'next'}).select('a')
        href = check_url[0]['href']
        return href
    return None


def get_all_page(url_une_categorie):
    """ doc """

    liste_de_toute_les_pages = []
    liste_de_toute_les_pages.append(url_une_categorie)
    check_href = verifie_si_plusieurs_page(url_une_categorie)
    if check_href != None:
        url_de_base = url_une_categorie.rsplit('/',1)
        page_url = url_de_base[0] + str("/" + check_href)
        autre_page = get_all_page(page_url)
        for test in autre_page:
            liste_de_toute_les_pages.append(test)
            
    return liste_de_toute_les_pages


def urls_books_categorys(url_page):
    """ get the books urls in one category"""
    urls_books_list = []
    page_book = requests.get(url_page)
    soupe = BeautifulSoup(page_book.content, 'html.parser')
    books = soupe.select('.product_pod')
    for book in books:
        titles = book.select('a')[1]['href']
        title = titles.replace('../../../',
                               'http://books.toscrape.com/catalogue/')
        urls_books_list.append(title)      
        
    return urls_books_list


def recuperer_tout_les_livres_pour_une_categories(urls):
    
    
    liste_urls_des_pages = []
    liste_informations_des_livres = []
    url_une_categorie = urls
    page_des_categories = get_all_page(url_une_categorie)
    for url in page_des_categories:
        urls_books = urls_books_categorys(url)
        for urls in urls_books:
            liste_urls_des_pages.append(urls)

    for infos_livres in liste_urls_des_pages:
        infos_data = get_data_in_dictionnarie(infos_livres)
        liste_informations_des_livres .append(infos_data)

    return liste_informations_des_livres



def url_categorys(soupe):
    """ get the url of the categories"""

    urls_cats_list = []
    urls_links = soupe.find('ul', {'class': 'nav-list'})
    urls_link = urls_links.findAll('a')
    for link in urls_link:
        urls_cats_list.append('http://books.toscrape.com/'
                              + link.get('href'))
    return urls_cats_list[1:51]


def write_books_data(all_books_list):
    """test list of dict in csv"""

    # books_list = book_list[0].keys()

    with open('bookinfosdatas.csv', 'w', encoding='utf-8_SIG',
              newline='') as csvfile:
        books = csv.DictWriter(csvfile, dialect='excel',
                               fieldnames= all_books_list[0].keys(),
                               delimiter=';')
        books.writeheader()
        books.writerows(all_books_list)


def main():
    """general function of the script"""

    url_site = 'https://books.toscrape.com/'
    page_book = requests.get(url_site)
    soupe = BeautifulSoup(page_book.content, 'html.parser')

    categories_urls = url_categorys(soupe)
    
    
    all_books_list = []
    for urls in categories_urls:
        all_data = recuperer_tout_les_livres_pour_une_categories(urls)
        #all_books_list.append(all_data)
        for books in all_data:
            all_books_list.append(books)
    write_books_data(all_books_list)
    
    return all_books_list

print(main())
