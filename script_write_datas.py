import csv


def write_books_data(infos_books_list):
    """ Save infos books for one category in en csv file"""

    csv_name = infos_books_list[0]["Category"]
    with open(f"{csv_name}.csv", "w", encoding="utf-8_SIG", newline="") as csvfile:
        books = csv.DictWriter(
            csvfile,
            dialect="excel",
            fieldnames=infos_books_list[0].keys(),
            delimiter=";",
        )
        books.writeheader()
        books.writerows(infos_books_list)


if __name__ == "__main__":
    write_books_data()