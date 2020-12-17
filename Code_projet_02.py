# mettre des parametres dans les fonctions, comprend if__name etc 


# import libraries
#import re
import csv
import requests
from bs4 import BeautifulSoup


# Set the Url i want to scrap

urlBook = 'http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html'
urlCategory = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'

'''
# Connect to the url
page_Book = requests.get(urlBook)

# Parse HTML and save in a BeautifulSoup Object
soupe = BeautifulSoup(page_Book.text, 'html.parser')
'''


# create the different functions with the parameter to scrap

# function for the title of the book
def title_one(one_title):
	"""Give the title of the book"""
	title = one_title.find(class_='active')
	return title.text

# function for the descrption of the book / autre solution??
def describ(one_resum):
    """give the resum of the book"""
    describ_01 = one_resum.findAll('p')[3]  #(string=re.compile("dragon"))
    return describ_01

# function for the product information of the book

def prod_info_th(allTh):
    """give the th"""
    # need tu do a list[] for all th
    list_th = []
    ths = allTh.findAll('tr')
    for tr in ths:
        a = tr.find('th')
        list_th.append(a.text)
    return list_th 


def prod_info_td(allTd):
    """give the td"""
    # need tu do a list[] for all td with append
    list_td = []
    tds = allTd.findAll('tr')
    for tr in tds:
        a = tr.find('td')
        list_td.append(a.text)
    return list_td
        
def prod_Category(category):
    category_01 = category.find(class_='page-header action')
    return category_01.text

def imageBook(image):
    '''Get the picture of the book'''
    imageBook = image.find(class_='item active')
    return imageBook


def getBook():
    '''all function to get a book'''
    page_Book = requests.get(urlBook)
    soupe = BeautifulSoup(page_Book.text, 'html.parser')
    page_Category = requests.get(urlCategory)
    soupeCat = BeautifulSoup(page_Category.text, 'html.parser')
    title = title_one(soupe)
    cat = prod_Category(soupeCat)
    resum = describ(soupe)
    info_produc = prod_info_th(soupe), prod_info_td(soupe)
    picture = imageBook(soupe)
    return title, cat, resum, info_produc, picture


getBook()


print(getBook())

'''
if __name__ == '__main__':
    main()
'''