import requests
from bs4 import BeautifulSoup
#"list-unstyled""Footer__Link""MHView""SearchResults""PropertyListingCard__Content MhHelper__Flex--spaced"
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup=BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

listings = soup.findAll("div", class_='PropertyListingCard')
print(listings)
