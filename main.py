#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

html_content = requests.get("https://www.stadt-koeln.de/leben-in-koeln/gesundheit/infektionsschutz/corona-virus/corona-virus-koeln-entwicklung-der-fallzahlen")

if html_content.ok:
    soup = BeautifulSoup(html_content.text, 'html.parser')
    table = soup.find_all("table")[1]
    for row, content in enumerate(table.find_all("tr")):
        if row == 0:
            continue
        date, infections = content.find_all("td")
        print("{}: {} infected".format(date.string, infections.string))
