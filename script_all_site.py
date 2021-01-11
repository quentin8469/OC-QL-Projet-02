#!/usr/bin/python
# -*- coding: utf-8 -*-
import script_one_book as sob
import script_writedata_csv as swc
import script_all_category as sac
import os


def main():
    """ general script for scraping"""

    scrap_book = sob.main()

    # scrap_category = sac.main()
    # swc.write_data_book(scrap_book)

    swc.write_books_data(scrap_book)

    # swc.write_category_csv(scrap_category)

    return scrap_book


if __name__ == '__main__':
    main()