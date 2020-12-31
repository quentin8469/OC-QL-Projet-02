import sys
import csv
import requests
from bs4 import BeautifulSoup

urlBook = 'https://books.toscrape.com/'
page_Book = requests.get(urlBook)
soupe = BeautifulSoup(page_Book.text, 'html.parser')

def all_Site_Category():
    urlBook = 'https://books.toscrape.com/'
    page_Book = requests.get(urlBook)
    soupe = BeautifulSoup(page_Book.text, 'html.parser')
    list_Category = []
    allCategory = soupe.find(class_='nav nav-list')
    list_Category.append(allCategory.text)
    return list_Category

print(all_Site_Category())


def main():
    Categories = all_Site_Category()
    writeDataBook(Categories )
    return Categories 




if __name__ == '__main__':
    main()