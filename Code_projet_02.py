import re
import csv
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html"

page = requests.get(url)
soupe = BeautifulSoup(page.text, 'html.parser')


def title_one():
	"""Give the title of the book"""
	title = soupe.find(class_='active')
	return title

print(title_one().text)

def describ():
    """give the resum of the book"""
    describ_01 = soupe.find(string=re.compile("dragon"))
    return describ_01

print(describ())

def prod_info():
	""" give productuc information th"""
	item = soupe.find('th')
	return item 

print(prod_info().text)

def prod_info_2():
	""" give productuc information td"""
	item_one = soupe.find('td')
	return  item_one

print(prod_info_2().text)

