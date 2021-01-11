#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv


def write_books_data(books_list):
    """test list of dict in csv"""

    # books_list = book_list[0].keys()

    with open('bookinfosdatas.csv', 'w', encoding='utf-8_SIG',
              newline='') as csvfile:
        books = csv.DictWriter(csvfile, dialect='excel',
                               fieldnames=books_list[0].keys(),
                               delimiter=';')
        books.writeheader()
        for book in books_list:
            books.writerows(books_list)


if __name__ == '__main__':
    main()