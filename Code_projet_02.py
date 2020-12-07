#code projet 02 web scraping
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html"

page = requests.get(url)

"""
if page.ok:
	soupe = BeautifulSoup(page.text, "html.parser")
	title = soupe.find('title')
	print(title.text)

"""



def title_one():
	"""Give the title of the book"""
	soupe = BeautifulSoup(page.text, "html.parser")
	title = soupe.find('title')
	return title

#
