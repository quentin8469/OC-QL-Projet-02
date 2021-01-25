#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_book_title(titre):
    """get the title of one book"""

    title = titre.find('h1')
    return title.text


def get_description_of_the_book(describ):
    """get the description of one book"""

    resum = describ.findAll('p')[3]
    return resum.text


def get_infos_produc_of_the_book(infos):
    """get all the produc informations of the book in a dictionnairy"""

    my_produc_infos = {}
    my_produc_infos['UPC '] = infos.findAll('td')[0].text
    my_produc_infos['Product Type '] = infos.findAll('td')[1].text
    my_produc_infos['Price (excl. tax) '] = infos.findAll('td')[2].text
    my_produc_infos['Price (incl. tax) '] = infos.findAll('td')[3].text
    my_produc_infos['Tax '] = infos.findAll('td')[4].text
    my_produc_infos['Availability '] = infos.findAll('td')[5].text
    my_produc_infos['Number of reviews '] = infos.findAll('td')[6].text
    return my_produc_infos


def get_book_category(cat):
    """get the category of one book"""

    category = cat.findAll('li')[2]
    return category.text.strip()


def get_product_page_url_of_a_book(url):
    """get the url of one book"""

    book_url = url
    return book_url


def get_book_image_url(image):
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
    book_data['Books_Url'] = get_product_page_url_of_a_book(url)
    book_data['Categorys'] = get_book_category(soupe)
    book_data['Titles'] = get_book_title(soupe)
    book_data['Resum'] = get_description_of_the_book(soupe)
    book_data['Producs_Infos'] = get_infos_produc_of_the_book(soupe)
    book_data['Images'] = get_book_image_url(soupe)
    return book_data


def get_all_book_info(url_book_list):
    """general function of the script, return all the book inforamtions."""
    
    #url = input('Enter the url of the book:  ')
    urls = url_book_list
    books = get_all_data_book(urls)
    return books


if __name__ == '__main__':
    get_all_book_info()