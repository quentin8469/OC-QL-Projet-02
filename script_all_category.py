#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv
import requests
from bs4 import BeautifulSoup


def all_site_category(soupe):
    """get the categories name"""
    
    list_categorys = []
    allcategory = soupe.find('ul', {'class': 'nav-list'})
    categorys = allcategory.findAll('li')
    for category in categorys:
        list_categorys.append(category.find('a').text.strip())
    return list_categorys


def url_categorys(soupe):
    """ get the categories url"""
    
    url_cat_list = []
    links = soupe.findAll('a')
    for link in links:
        url_cat_list.append('http://books.toscrape.com/' + link.get('href'))
    return url_cat_list
    
    
def main():
    """general function of the script"""
    
    urlbook = 'https://books.toscrape.com/'
    page_book = requests.get(urlbook)
    soupe = BeautifulSoup(page_book.text, 'html.parser')
    categories_name = all_site_category(soupe)
    categories_urls = url_categorys(soupe)
    #writeDataBook(Categories )
    return categories_name, categories_urls



if __name__ == '__main__':
    main()

print(main())