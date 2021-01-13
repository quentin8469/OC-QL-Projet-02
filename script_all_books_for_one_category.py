#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
import script_one_book as sob
import script_writedata_csv as swc

def url_categorys(soupe):
    """ get the books urls in one category"""

    urls_books_list = []
    books = soupe.select('.product_pod')

    for book in books:
        titles = book.select('a')[1]['href']
        title = titles.replace('../../../',
                               'http://books.toscrape.com/catalogue/')
        urls_books_list.append(title)
    return urls_books_list


def get_all_url_in_category(urls_list):
    """general function of the script"""

    
    #url_category = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    url_category = urls_list
    page_book = requests.get(url_category)
    soupe = BeautifulSoup(page_book.content, 'html.parser')
    books_list_url = url_categorys(soupe)
    
    
    books_list =[]
    for book in books_list_url:
        infos = sob.get_all_book_info(book)
        books_list.append(infos)
    #swc.write_books_data(books_list)
    
    return books_list


if __name__ == '__main__':
    get_all_url_in_category()

#print(get_all_url_in_category())