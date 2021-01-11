#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import script_writedata_csv as swc

def get_book_title(titre):
    """get the title of one book"""

    title = titre.find('h1')
    return title.text


def description_of_the_book(describ):
    """get the description of one book"""

    resum = describ.findAll('p')[3]
    return resum.text


def infos_produc(infos):
    """get all the produc information of the book in a dictionnairy"""

    my_produc_infos = {}

    my_produc_infos['UPC '] = infos.findAll('td')[0].text
    my_produc_infos['Product Type '] = infos.findAll('td')[1].text
    my_produc_infos['Price (excl. tax) '] = infos.findAll('td'
            )[2].text
    my_produc_infos['Price (incl. tax) '] = infos.findAll('td'
            )[3].text
    my_produc_infos['Tax '] = infos.findAll('td')[4].text
    my_produc_infos['Availability '] = infos.findAll('td')[5].text
    my_produc_infos['Number of reviews '] = infos.findAll('td'
            )[6].text
    return my_produc_infos


def category(cat):
    """get the category of one book"""

    category = cat.findAll('li')[2]
    return category.text.strip()


def product_page_url(url):
    """get the url of one book"""
    
    #modifier nom variable
    #urls = url.findAll('a')[3]
    #urlss = urls.get('href')
    #urlsss = 'http://books.toscrape.com' + urlss
    book_url = url
    return book_url


def image_url(image):
    """get the picture of the book"""

    image_book = image.find('img').get('src')
    url_image = image_book.replace('../../',
                                   'http://books.toscrape.com/')
    return url_image


def get_all_data_book(url):
    """ get all data of one book and take all in a dictionnairie for writing in a csv file"""

    html = requests.get(url)
    soupe = BeautifulSoup(html.content, 'html.parser')
    book_data = {}
    book_data['Urls'] = product_page_url(url)
    book_data['Categorys'] = category(soupe)
    book_data['Titles'] = get_book_title(soupe)
    book_data['Resum'] = description_of_the_book(soupe)
    book_data['Producs_Infos'] = infos_produc(soupe)
    book_data['Images'] = image_url(soupe)
    return book_data


def main(url_book_list):
    """general function of the script"""
    
    books_list =[]
    #url = input('Enter the url of the book:  ')
    url = url_book_list
    books = get_all_data_book(url)
    for book in books:
        books_list.append(book)
    tttt
    #swc.write_books_data(books_list)
    return print(books_list)



if __name__ == '__main__':
    main()