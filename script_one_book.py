#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv
import requests
from bs4 import BeautifulSoup


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

    my_produc_infos['UPC: '] = infos.findAll('td')[0].text
    my_produc_infos['Product Type : '] = infos.findAll('td')[1].text
    my_produc_infos['Price (excl. tax) : '] = infos.findAll('td'
            )[2].text
    my_produc_infos['Price (incl. tax) : '] = infos.findAll('td'
            )[3].text
    my_produc_infos['Tax : '] = infos.findAll('td')[4].text
    my_produc_infos['Availability : '] = infos.findAll('td')[5].text
    my_produc_infos['Number of reviews : '] = infos.findAll('td'
            )[6].text
    return my_produc_infos


def category(cat):
    """get the category of one book"""

    category = cat.findAll('li')[2]
    return category.text


def product_page_url(url):
    """get the url of one book"""

    urls = url.findAll('a')[3]
    urlss = urls.get('href')
    urlsss = 'http://books.toscrape.com' + urlss
    return urlsss


def image_url(image):
    """get the picture of the book"""

    image_book = image.find('img')
    path_image = image_book.get('src')
    url_image = path_image.replace('../../',
                                   'http://books.toscrape.com/')
    return url_image


def get_all_data_book():
    """ get all data of one book and take all in a dictionnairie for writing in a csv file"""

    url = input('Enter the url of the book, category or the site:  ')
    html = requests.get(url)
    soupe = BeautifulSoup(html.text, 'html.parser')
    book_data = {}
    book_data['Urls'] = product_page_url(soupe)
    book_data['Categorys'] = category(soupe)
    book_data['Titles'] = get_Book_title(soupe)
    book_data['Resum'] = description_of_the_book(soupe)
    book_data['Producs_Infos'] = infos_produc(soupe)
    book_data['Images'] = image_url(soupe)
    return book_data


def write_data_book(books):
    ''' write the data of the book in a csv file'''

    with open('bookinfos.csv', 'w', encoding='utf-8', newline='') as \
        csvfile:
        fieldnames = [
            'Urls',
            'Categorys',
            'Titles',
            'Resum',
            'Producs_Infos',
            'Images',
            ]
        book = csv.DictWriter(csvfile, fieldnames=fieldnames,
                              delimiter=';')
        book.writeheader()
        book.writerow(books)


def main():
    books = get_all_data_book()
    write_data_book(books)
    return books


if __name__ == '__main__':
    main()