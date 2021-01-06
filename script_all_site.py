import script_one_book as sob
import script_writedata_csv as swc
import os


def main():
    """ general script for scraping"""
    
    scrap_book = sob.main()
    swc.write_data_book(scrap_book)
    return scrap_book

if __name__=='__main__':
    main()