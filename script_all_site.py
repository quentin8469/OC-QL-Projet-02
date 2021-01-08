import script_one_book as sob
import script_writedata_csv as swc
import script_all_category as sac
import os



"""
def urls_titles():
    titles_urls = []

    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    for i in range (1,2):
        scrape_url = base_url.format(i)
        html = requests.get(url)
        soupe = BeautifulSoup(html.text, 'html.parser')
        books = soupe.select('.product_pod')

        for book in books:
            titles = book.select('a')[1]['href']
            title = 'http://books.toscrape.com/' + titles
            titles_urls.append(title)
    return titles_urls     

print(urls_titles())

"""



def main():
    """ general script for scraping"""
    
    scrap_book = sob.main()
    scrap_category = sac.main()
    swc.write_data_book(scrap_book)
    #swc.write_category_csv(scrap_category)
    return scrap_book, scrap_category

if __name__=='__main__':
    main()