import csv


def write_data_book(books):
    ''' write the data of the book in a csv file'''

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

def write_category_csv(name, urls):
    """write the categories url and name in a csv file"""

    with open('catsinfos.csv', 'w', encoding='utf-8', newline='') as \
        csvfile:
        catwriter = csv.writer(csvfile,delimiter=';')
        catwriter.writerow(name)
        catwriter.writerow(urls)
        
        
if __name__=='__main__':
    main()