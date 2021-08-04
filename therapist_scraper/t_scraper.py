import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
import regex

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

records = []
next_url = "https://www.psychologytoday.com/us/therapists/or/portland/108093?sid=610a32c3d201b&ref=1"
for person in range(10):

    next_page = requests.get(next_url, headers=headers)
    next_soup = BeautifulSoup(next_page.content, "html.parser")
    next_zip_code = next_soup.find(itemprop="postalcode").get_text()
    next_name = next_soup.find(itemprop="name").get_text()
    next_title = next_soup.find("h2").get_text()
    try:
        next_specialties = next_soup.find("ul", class_="attribute-list specialties-list").get_text()
    except AttributeError:
        next_specialties = "N/A"
    # next_insurance = next_soup.find("ul", class_= "attribute-list copy-small").get_text()
    try:
        next_price = next_soup.find("div", class_="finances-office").get_text().split('\n')
        while '' in next_price:
            next_price.remove('')
        while '            ' in next_price:
            next_price.remove('            ')
        while '                                                    ' in next_price:
            next_price.remove('                                                    ')
        price = next_price[0]
    except AttributeError:
        price = "N/A"
    
    
    records.append((next_name.strip(), next_zip_code, next_title, next_specialties, price))

    
    time.sleep(1)
    next_url = next_soup.find("a", class_="profile-next")["href"]

df = pd.DataFrame(records, columns=["name","zip","title","specialties","price"])

df["specialties"] = df["specialties"].str.replace(' ','')

df[["title","specialties","price"]] = df[["title","specialties","price"]].replace('\n',' ', regex=True)

df["price"] = df["price"].str.replace('Cost per Session: ','')

df["price"] = df["price"].str.replace(' ','')

df["title"] = df["title"].str.replace(' ','')

df.to_csv('therapist_data.csv')