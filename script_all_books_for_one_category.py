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


def main():
    """general function of the script"""

    url_category = \
        'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    page_book = requests.get(url_category)
    soupe = BeautifulSoup(page_book.content, 'html.parser')
    books_list_url = url_categorys(soupe)
   
    
    #book = sob.main(books_list_url)
   
    return books_list_url


if __name__ == '__main__':
    main()

print(main())


            