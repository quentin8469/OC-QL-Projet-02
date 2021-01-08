#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    urls_cats_list = []
    urls_links = soupe.find('ul', {'class': 'nav-list'})
    urls_link = urls_links.findAll('a')
    for link in urls_link:
        urls_cats_list.append('http://books.toscrape.com/'
                            + link.get('href'))
    return urls_cats_list


def write_category_csv(name, urls):
    """write the categories url and name in a csv file"""

    with open('catsinfos.csv', 'w', encoding='utf-8', newline='') as \
        csvfile:
        catwriter = csv.writer(csvfile, delimiter=';')
        
        catwriter.writerow(name)
        catwriter.writerow(urls)


def main():
    """general function of the script"""

    urlbook = 'https://books.toscrape.com/'
    page_book = requests.get(urlbook)
    soupe = BeautifulSoup(page_book.text, 'html.parser')
    categories_name = all_site_category(soupe)
    categories_urls = url_categorys(soupe)
    write_category_csv(categories_name, categories_urls)
    return (categories_name, categories_urls)


if __name__ == '__main__':
    main()

print (main())

            