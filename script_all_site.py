#!/usr/bin/python
# -*- coding: utf-8 -*-
import script_one_book as sob
import script_all_category as sac
import script_all_books_for_one_category as sabfoc
#import script_writedata_csv as swc
#import os


def main():
    """ general script for scraping"""

    scrap_all_cat = sac.main()
    scrap_books_cat = sabfoc.main()
    #scrap_book = sob.main()
    # swc.write_data_book(scrap_book)
    #swc.write_books_data(scrap_book)
    # swc.write_category_csv(scrap_category)

    return  print(scrap_all_cat), print(scrap_books_cat)

if __name__ == '__main__':
    main()

            