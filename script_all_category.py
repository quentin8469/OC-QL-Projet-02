import sys
import csv
import requests
from bs4 import BeautifulSoup

urlBook = 'https://books.toscrape.com/'
page_Book = requests.get(urlBook)
soupe = BeautifulSoup(page_Book.text, 'html.parser')

def all_site_category():
    urlBook = 'https://books.toscrape.com/'
    page_Book = requests.get(urlBook)
    soupe = BeautifulSoup(page_Book.text, 'html.parser')
    list_Categorys = []
    #allCategory = soupe.findAll('ul', {"class": "nav-list"})
    allCategory = soupe.find('ul', {'class': 'nav-list'})
    categorys = allCategory.findAll('li')
    for category in categorys:
        list_Categorys.append(category.find('a').text.strip())
    return list_Categorys



def main():
    categories = all_site_category()
    #writeDataBook(Categories )
    return categories 



if __name__ == '__main__':
    main()

print(all_site_category())