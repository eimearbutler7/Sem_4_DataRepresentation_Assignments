import requests
from bs4 import BeautifulSoup
import csv
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup=BeautifulSoup(page.content, 'html.parser')
#print(soup.preffity())

home_file = open('c:/Users/Eimear/Documents/GitHub/Sem_4_DataRepresentation_Assignments/Week 3/week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")
#print(listings)
entry=[]
for listing in listings:
    price = listing.findAll(class_="PropertyListingCard_Price").text
    entry.append(price)
    address = listing.findAll(class_="PropertyListingCard_Address").text
    entry.append(address)
#print(entry)

home_writer.writerow(entry)
home_file.close()