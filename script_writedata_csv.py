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


if __name__=='__main__':
    main()