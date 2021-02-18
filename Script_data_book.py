import requests
from bs4 import BeautifulSoup
import os


def get_product_page_url(url_du_livre):
    """ get url of a book """

    book_url = url_du_livre
    return book_url


def get_universal_product_code(soupe):
    """ get UPC of a book """

    upc = soupe.find_all("td")[0].text
    return upc


def get_title(soupe):
    """ get the title of a book """

    title = soupe.find("h1").text
    return title


def get_price_including_tax(soupe):
    """ get the price with the tax of a book """

    price_including_tax = soupe.find_all("td")[3].text
    return price_including_tax


def get_price_excluding_tax(soupe):
    """ get the price of a book excludinf tax """

    price_excluding_tax = soupe.find_all("td")[2].text
    return price_excluding_tax


def get_tax(soupe):
    """ get the price of the tax of a book """

    tax = soupe.find_all("td")[4].text
    return tax


def get_number_available(soupe):
    """ get the number of a book in stock """

    number_available = soupe.find_all("td")[5].text
    return number_available


def get_product_description(soupe):
    """ give the description of the story for a book """

    product_description = soupe.find_all("p")[3].text
    return product_description


def get_category(soupe):
    """ give the category of a book """

    category = soupe.find_all("li")[2].text.strip()
    return category


def get_review_rating(soupe):
    """ give the number of star for a book """

    review_rating = soupe.find_all("td")[6].text
    return review_rating


def get_image_url(soupe):
    """ give the picture url of a book """

    image_book = soupe.find("img").get("src")
    url_image = image_book.replace("../../", "http://books.toscrape.com/")
    return url_image


def picture_directory(cat_image):
    """ create pictures directory for one category """

    try:
        os.mkdir(cat_image)
    except:
        pass
    try:
        os.chdir(cat_image)
    except:
        pass


def download_picture(soupe):
    """ download pictures in directory """

    cat_image = get_category(soupe)
    picture_directory(cat_image)
    picture_title = get_universal_product_code(soupe)
    url_image = get_image_url(soupe)
    lien_image = requests.get(url_image)
    with open(f"{cat_image}_{picture_title}.jpg", "wb") as dl_image:
        dl_image.write(lien_image.content)

    local = os.getcwd()
    os.chdir("../")
    return local


def get_data_in_dictionnarie(url_books):
    """ get all data of one book in a dictionnarie """

    html = requests.get(url_books)
    soupe = BeautifulSoup(html.content, "html.parser")
    book_data = {}
    book_data["Book_Url"] = get_product_page_url(url_books)
    book_data["Category"] = get_category(soupe)
    book_data["Titles"] = get_title(soupe)
    book_data["Description"] = get_product_description(soupe)
    book_data["UPC"] = get_universal_product_code(soupe)
    book_data["Price_including_tax"] = get_price_including_tax(soupe)
    book_data["Price_excluding_tax"] = get_price_excluding_tax(soupe)
    book_data["Tax "] = get_tax(soupe)
    book_data["Number_available"] = get_number_available(soupe)
    book_data["Review_rating"] = get_review_rating(soupe)
    book_data["Image_url"] = get_image_url(soupe)
    book_data["local_Image_path"] = download_picture(soupe)
    return book_data


if __name__ == "__main__":
    get_data_in_dictionnarie()