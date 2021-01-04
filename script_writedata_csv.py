
import csv


"""

''' write the data of the book in a csv file'''
headers = [['titre'], ['category'], ['resum'], ['produc'], ['image']]
with open('bookinfosss.csv', 'w', encoding='utf-8', newline= '') as csvfile:
    book = csv.writer(csvfile, delimiter=',')
    for ligne in headers:
        book.writerow(ligne)
"""

dico = {}
dico['titre'] = '0'
dico['image'] = 'gghj'
dico['truc'] = 'azerty'
    
with open('dico.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['titre', 'image', 'truc']
	
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerow(dico)

