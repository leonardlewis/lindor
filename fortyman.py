from bs4 import BeautifulSoup as bs
from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve)

team = input("What team do you want to look up? (Enter a city abbreviation such as 'cle' or 'sf'.)  ")

html_doc = urlopen(f"http://m.mlb.com/{team}/roster/40-man/")

soup = bs(html_doc, 'html.parser')

tables = soup.findAll("table", { "class" : "data roster_table" })
for table in tables:
    table_body = table.find("tbody")
    for row in table_body.findAll("tr"):
        names = row.find("td", {"class" : "dg-name_display_first_last"}, "string").contents
        names = names[1].contents
        print(names[0])
