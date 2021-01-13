#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
import script_all_books_for_one_category as sabfoc
import script_writedata_csv as swc


def url_categorys(soupe):
    """ get the url of the categories"""

    urls_cats_list = []
    urls_links = soupe.find('ul', {'class': 'nav-list'})
    urls_link = urls_links.findAll('a')
    for link in urls_link:
        urls_cats_list.append('http://books.toscrape.com/'
                              + link.get('href'))
    return urls_cats_list[1:51]


def urls_book_in_category():
    """ get a list of urls book in one category"""


def main():
    """general function of the script"""

    url_site = 'https://books.toscrape.com/'
    page_book = requests.get(url_site)
    soupe = BeautifulSoup(page_book.content, 'html.parser')

    categories_urls = url_categorys(soupe)
    
    
    urls_list = []
    for urls in categories_urls:
        category = sabfoc.get_all_url_in_category(urls)
        urls_list.append(category)
    swc.write_books_data(urls_list)
    
    return urls_list


if __name__ == '__main__':
    main()

print(main())   