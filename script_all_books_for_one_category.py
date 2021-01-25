#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
import script_one_book as sob
import script_writedata_csv as swc


'''
def url_categorys(url_page):# def url_page():
    """ get the books urls in one category"""

    urls_books_list = []
    page_book = requests.get(page_url)
    soupe = BeautifulSoup(page_book.content, 'html.parser')
    books = soupe.select('.product_pod')

    for book in books:
        titles = book.select('a')[1]['href']
        title = titles.replace('../../../',
                               'http://books.toscrape.com/catalogue/')
        urls_books_list.append(title)
        

    return urls_books_list
'''

def check_next_page(url_category):
    """ get a list of page in one category"""
    
    page_book = requests.get(url_category)
    soupe = BeautifulSoup(page_book.content, 'html.parser')
    
    test_list = []
    next_page = soupe.find("li",class_="next")
    if next_page != None:
        link = soupe.find("li",class_="next").select('a')
        next_page_href = link[0]['href']
        url_page = url_category.replace('index.html', next_page_href)
        test_list.append(page_url)
        last_page = check_next_page(url_page)
    else:
        test_list.append(url_category)
        
    return test_list
    

def get_all_url_in_category(urls):
    """general function of the script"""

    
    #url_page = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    url_category = urls
    #page_book = requests.get(url_category)
    #soupe = BeautifulSoup(page_book.content, 'html.parser')
    next_page = check_next_page(url_category)
    #books_list_url = url_categorys(next_page)
    
    '''
    books_list =[]
    for book in books_list_url:
        infos = sob.get_all_book_info(book)
        books_list.append(infos)
    #swc.write_books_data(books_list)
    '''
    return next_page


if __name__ == '__main__':
    get_all_url_in_category()

#print(get_all_url_in_category())