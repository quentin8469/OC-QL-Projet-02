import re
import csv
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html"

page = requests.get(url)
soupe = BeautifulSoup(page.text, 'html.parser')

print('\n')#saut de ligne

# function for the title of the book
def title_one():
	"""Give the title of the book"""
	title = soupe.find(class_='active')
	return title

print(title_one().text)

print('\n')#saut de ligne

# function for the descrption of the book / autre solution??
def describ():
    """give the resum of the book"""
    describ_01 = soupe.find(string=re.compile("dragon"))
    return describ_01

print(describ())

print('\n')#saut de ligne

# function for the product information of the book

def prod_info_th():
    """give the th"""
    ths = soupe.findAll('tr')
    for tr in ths:
        a = tr.find('th')
        print(a.text)
    
    
def prod_info_td():
    """give the td"""
    tds = soupe.findAll('tr')
    for tr in tds:
        a = tr.find('td')
        print(a.text)



print (prod_info_th())
print('\n')#saut de ligne
print (prod_info_td())
print('\n')#saut de ligne
