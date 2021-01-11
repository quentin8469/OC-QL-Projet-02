#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup


def url_categorys(soupe):
    """ get the url of the categories"""

    urls_cats_list = []
    urls_links = soupe.find('ul', {'class': 'nav-list'})
    urls_link = urls_links.findAll('a')
    for link in urls_link:
        urls_cats_list.append('http://books.toscrape.com/'
                              + link.get('href'))
    return urls_cats_list


def main():
    """general function of the script"""

    urlbook = 'https://books.toscrape.com/'
    page_book = requests.get(urlbook)
    soupe = BeautifulSoup(page_book.text, 'html.parser')
    categories_urls = url_categorys(soupe)

    return categories_urls


if __name__ == '__main__':
    main()

#print(main())