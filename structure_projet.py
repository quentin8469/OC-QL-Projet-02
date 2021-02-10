import requests
from bs4 import BeautifulSoup
import csv342 as csv
import os

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

def picture_directory(cat_image):
    """ create pictures directory for one category """
    try:
        os.mkdir(cat_image)
    except:
        pass
    try:
        os.chdir(cat_image)
    except:
        pass
    


def download_picture(soupe):
    """ download pictures in directory """

    cat_image = get_category(soupe)
    picture_directory(cat_image)

    picture_title = get_universal_product_code(soupe)
    url_image = get_image_url(soupe)
    lien_image = requests.get(url_image)
    
    with open(f'{cat_image}_{picture_title}.jpg','wb') as dl_image:
        dl_image.write(lien_image.content)
    
    local = os.getcwd()
    os.chdir('../')
    return local

 
def get_data_in_dictionnarie(url_books):
    """ doc """
    
    html = requests.get(url_books)
    soupe = BeautifulSoup(html.content, 'html.parser')
    
    book_data = {}
    
    book_data['Book_Url'] = get_product_page_url(url_books)
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
    book_data['local_Image_url'] = download_picture(soupe)
    
    return book_data
   

def check_number_pages(url_actuelle):
    """ doc """
    
    html = requests.get(url_actuelle)
    soupe = BeautifulSoup(html.content, 'html.parser')
    check_url = soupe.find('li', {'class': 'next'})
    if check_url != None:
        check_url = soupe.find('li', {'class': 'next'}).select('a')
        href = check_url[0]['href']
        return href
    return None


def get_all_page(url_one_categorie):
    """ doc """

    liste_all_pages = []
    liste_all_pages.append(url_one_categorie)
    check_href = check_number_pages(url_one_categorie)
    if check_href != None:
        url_de_base = url_one_categorie.rsplit('/',1)
        page_url = url_de_base[0] + str("/" + check_href)
        other_page = get_all_page(page_url)
        for page in other_page:
            liste_all_pages.append(page)
            
    return liste_all_pages


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


def get_all_books_for_one_category(urls):
    
    
    urls_liste_pages = []
    infos_books_list = []
    url_one_categorie = urls
    urls_categories_pages = get_all_page(url_one_categorie)
    for url_page in urls_categories_pages:
        urls_books = urls_books_categorys(url_page)
        for urls in urls_books:
            urls_liste_pages.append(urls)

    for url_books in urls_liste_pages:
        infos_data = get_data_in_dictionnarie(url_books)
        infos_books_list.append(infos_data)
    write_books_data(infos_books_list)
    return infos_books_list



def url_categorys(soupe):
    """ get the url of the categories"""

    urls_cats_list = []
    urls_links = soupe.find('ul', {'class': 'nav-list'})
    urls_link = urls_links.findAll('a')
    for link in urls_link:
        href = f"http://books.toscrape.com/{link.get('href')}"
        urls_cats_list.append(href)
    return urls_cats_list[1:51]


def write_books_data(infos_books_list):
    """test list of dict in csv"""

    
    csv_name = infos_books_list[0]['Category']

    with open(f'{csv_name}.csv', 'w', encoding='utf-8_SIG',
              newline='') as csvfile:
        books = csv.DictWriter(csvfile, dialect='excel',
                               fieldnames= infos_books_list[0].keys(),
                               delimiter=';')
        books.writeheader()
        books.writerows(infos_books_list)


def main():
    """general function of the script"""

    url_site = 'https://books.toscrape.com/'
    page_book = requests.get(url_site)
    soupe = BeautifulSoup(page_book.content, 'html.parser')

    categories_urls = url_categorys(soupe)
    
    
    all_books_list = []
    for urls in categories_urls:
        all_data = get_all_books_for_one_category(urls)
   
        for books in all_data:
            all_books_list.append(books)
    
    return 


if __name__ == '__main__':
    
    directory_name = 'book_scraping'
    try:
        os.mkdir(directory_name)
    except:
        print('dossier deja existant')

    os.chdir(directory_name)
    main()
