import urllib.request
import bs4
from bs4 import BeautifulSoup
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page)
print(soup)