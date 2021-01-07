import sys
import csv
import requests
from bs4 import BeautifulSoup


def all_site_category():
    urlbook = 'https://books.toscrape.com/'
    page_book = requests.get(urlbook)
    soupe = BeautifulSoup(page_book.text, 'html.parser')
    list_categorys = []
    allcategory = soupe.find('ul', {'class': 'nav-list'})
    categorys = allcategory.findAll('li')
    for category in categorys:
        list_categorys.append(category.find('a').text.strip())
    return list_categorys



def main():
    categories = all_site_category()
    #writeDataBook(Categories )
    return categories 



if __name__ == '__main__':
    main()

print(all_site_category())