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


"""
def writeDataBook(books):
    ''' write the data of the book in a csv file'''
    with open('bookinfos.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Urls', 'Categorys', 'Titles', 'Resum', 'Producs_Infos', 'Images']
        book = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        book.writeheader()
        book.writerow(books)
"""
def main():
    Categories = all_Site_Category()
    writeDataBook(Categories )
    return Categories 



if __name__ == '__main__':
    main()

print(all_Site_Category())