import requests
import urllib.request
import time
from bs4 import BeautifulSoup

URL = "https://www.psychologytoday.com/us/therapists/or/portland/841246?sid=610343265d839&ref=10"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

zip_code = soup.find(itemprop="postalcode").get_text()

name = soup.find(itemprop="name").get_text()

title = soup.find("h2").get_text()

specialties = soup.find("ul", class_="attribute-list specialties-list").get_text()

insurance = soup.find("ul", class_= "attribute-list copy-small").get_text()
#price = soup.find("div", class_="finances-office").get_text()


print(name.strip())
print(zip_code)
print(specialties)
print(title.strip())
print(insurance)