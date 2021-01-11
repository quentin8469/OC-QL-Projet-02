import csv

"""
def write_data_book(books):
    ''' write the data of the book in a csv file'''
    #keys = books[0].keys()
    with open('bookinfos.csv', 'w', encoding='utf-8', newline='') as \
        csvfile:
        fieldnames = [
            'Urls',
            'Categorys',
            'Titles',
            'Resum',
            'Producs_Infos',
            'Images',
            ]
        book = csv.DictWriter(csvfile, fieldnames=fieldnames,
                              delimiter=';')
        book.writeheader()
        book.writerow(books)
"""

def write_books_data(books_list):
    """test list of dict in csv"""
    
    #books_list = book_list[0].keys()
    with open('bookinfosdatas.csv', 'w', encoding='utf-8_SIG', newline='') as csvfile:
        books = csv.DictWriter(csvfile,dialect='excel', fieldnames=books_list[0].keys(), delimiter=';')
        books.writeheader()
        for book in books_list:
            books.writerows(books_list)
        

"""
import csv

toCSV = [{'name':'bob','age':25,'weight':200},
         {'name':'jim','age':31,'weight':180}]
with open('people.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=toCSV[0].keys(),

                       )
    fc.writeheader()
    fc.writerows(toCSV)
    
    
"""
'''
def write_category_csv(name, urls):
    """write the categories url and name in a csv file"""

    with open('catsinfos.csv', 'w', encoding='utf-8', newline='') as \
        csvfile:
        catwriter = csv.writer(csvfile,delimiter=';')
        catwriter.writerow(name)
        catwriter.writerow(urls)
        
'''
        
if __name__=='__main__':
    main()