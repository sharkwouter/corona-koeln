#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

html_content = requests.get("https://www.stadt-koeln.de/leben-in-koeln/gesundheit/infektionsschutz/corona-virus/corona-virus-koeln-entwicklung-der-fallzahlen")

if html_content.ok:
    soup = BeautifulSoup(html_content.text, 'html.parser')
    tables = soup.find_all("table")
    for table_number, table in enumerate(tables):
        print("\n{}".format(table_number))
        for row, content in enumerate(table.find_all("tr")):
            # Skip the header row
            # if row == 0:
            #     continue
            row_string = "Row {}: ".format(row)
            for item in content.find_all("td"):
                row_string = "{}{},".format(row_string, item.string)
            print(row_string)
