import requests
import urllib.request
import time
from bs4 import BeautifulSoup


URL =  "https://www.psychologytoday.com/us/therapists/or/portland/170401?sid=610587f4f295d&ref=4"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

zip_code = soup.find(itemprop="postalcode").get_text()

name = soup.find(itemprop="name").get_text()

title = soup.find("h2").get_text()

specialties = soup.find("ul", class_="attribute-list specialties-list").get_text()

insurance = soup.find("ul", class_= "attribute-list copy-small").get_text()
price = soup.find("div", class_="finances-office").get_text()


print(name.strip())
print(zip_code)
print(specialties)
print(title.strip())
#print(insurance)
print(price)

# next_url = soup.find("a", class_="profile-next")["href"]


# print(next_url)

# next_page = requests.get(next_url, headers=headers)

# next_soup = BeautifulSoup(next_page.content, "html.parser")

# next_zip_code = next_soup.find(itemprop="postalcode").get_text()

# next_name = next_soup.find(itemprop="name").get_text()

# next_title = next_soup.find("h2").get_text()

# next_specialties = next_soup.find("ul", class_="attribute-list specialties-list").get_text()

# next_insurance = next_soup.find("ul", class_= "attribute-list copy-small").get_text()

# next_price = next_soup.find("div", class_="finances-office").get_text()


# print(next_name.strip())
# print(next_zip_code)
# print(next_specialties)
# print(next_title.strip())
# #print(insurance)
# print(next_price)

next_url = "https://www.psychologytoday.com/us/therapists/or/portland/170401?sid=610587f4f295d&ref=4"
for person in range(7):

  next_page = requests.get(next_url, headers=headers)

  next_soup = BeautifulSoup(next_page.content, "html.parser")

  next_zip_code = next_soup.find(itemprop="postalcode").get_text()

  next_name = next_soup.find(itemprop="name").get_text()

  next_title = next_soup.find("h2").get_text()

  next_specialties = next_soup.find("ul", class_="attribute-list specialties-list").get_text()

  next_insurance = next_soup.find("ul", class_= "attribute-list copy-small").get_text()

  next_price = next_soup.find("div", class_="finances-office").get_text()


  print(next_name.strip())
  # print(next_zip_code)
  # print(next_specialties)
  # print(next_title.strip())
  # #print(insurance)
  # print(next_price)

  next_url = next_soup.find("a", class_="profile-next")["href"]
