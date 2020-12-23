import sys
import csv
import requests
from bs4 import BeautifulSoup

def get_Book_Title(titre):
    title = titre.find('h1')
    return(title.text)


def description_Of_The_Book(describ):
    resum = describ.findAll('p')[3]
    return(resum.text)
	
def infos_Produc(infos):
    my_Produc_Infos ={
    
    }
    my_Produc_Infos['UPC: '] = infos.findAll('td')[0].text
    my_Produc_Infos['Product Type : '] = infos.findAll('td')[1].text
    my_Produc_Infos['Price (excl. tax) : '] = infos.findAll('td')[2].text
    my_Produc_Infos['Price (incl. tax) : '] = infos.findAll('td')[3].text
    my_Produc_Infos['Tax : '] = infos.findAll('td')[4].text
    my_Produc_Infos['Availability : '] = infos.findAll('td')[5].text
    my_Produc_Infos[ 'Number of reviews : '] = infos.findAll('td')[6].text
    return my_Produc_Infos

def category(cat):
    category = cat.findAll('li')[2]
    return(category.text)


def image_Url(image):
    image_Book = image.find('img')
    path_image = image_Book.get('src')
    url_image = path_image.replace("../../","http://books.toscrape.com/")
    return(url_image)

def get_All_Data_Book():
    url = input('Enter the url of the book, category or the site:  ')
    html = requests.get(url)
    soupe = BeautifulSoup(html.text, 'html.parser')
    Book_Data = {}
    #Book [urls] = product_Page_Url(soupe)
    Book_Data ['categorys'] = category(soupe)
    Book_Data ['titles'] = get_Book_Title(soupe)
    Book_Data ['resum'] = description_Of_The_Book(soupe)
    Book_Data ['producs_Infos'] = infos_Produc(soupe)
    Book_Data ['images'] = image_Url(soupe)
    return Book_Data

def writeDataBook(books):
	''' write the data of the book in a csv file'''
	headers = ['titre', 'category', 'resum', 'produc', 'image']
	with open('bookinfos.csv', 'w', encoding='utf-8', newline='') as csvfile:
		book = csv.writer(csvfile, delimiter='_')
		book.writerow(headers)
		book.writerow(books)


def main():
    books = get_All_Data_Book()
    writeDataBook(books)
    return books


if __name__ == '__main__':
    main()
    

print(main())

"""
import sys
import csv
import requests
from bs4 import BeautifulSoup

urlBook = 'https://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html'
page_Book = requests.get(urlBook)
soupe = BeautifulSoup(page_Book.text, 'html.parser')

def get_Book_Title():
    title = soupe.find('h1')
    return(title.text)

def description_Of_The_Book():
    resum = soupe.findAll('p')[3]
    return(resum.text)
	
def infos_Produc():
    my_Produc_Infos ={
    
    }
    my_Produc_Infos['UPC: '] = soupe.findAll('td')[0].text
    my_Produc_Infos['Product Type : '] = soupe.findAll('td')[1].text
    my_Produc_Infos['Price (excl. tax) : '] = soupe.findAll('td')[2].text
    my_Produc_Infos['Price (incl. tax) : '] = soupe.findAll('td')[3].text
    my_Produc_Infos['Tax : '] = soupe.findAll('td')[4].text
    my_Produc_Infos['Availability : '] = soupe.findAll('td')[5].text
    my_Produc_Infos[ 'Number of reviews : '] = soupe.findAll('td')[6].text
    return my_Produc_Infos

def category():
    category = soupe.findAll('li')[2]
    return(category.text)

def image_Url():
    image_Book = soupe.find('img')
    path_image = image_Book.get('src')
    url_image = path_image.replace("../../","http://books.toscrape.com/")
    return(url_image)
	
print(get_Book_Title())
print(category())
print(description_Of_The_Book())
print(infos_Produc())
print(image_Url())
"""