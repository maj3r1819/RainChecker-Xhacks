from bs4 import BeautifulSoup
import requests
import lxml
import json
import re

headers = {  # <-- so the Google will treat your script as a "real" user browser.
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '+', s)

    return s


product = input("enter query:")
product = urlify(product)

response = requests.get(
  'https://www.google.com/search?q='+ product +'&tbm=shop',
  headers=headers).text

soup = BeautifulSoup(response, 'lxml')

data = []

for container in soup.findAll('div', class_='sh-dgr__content'):
    title = container.find('h4', class_='A2sOrd').text
    price = container.find('span', class_='a8Pemb').text
    supplier = container.find('div', class_='aULzUe IuHnof').text
    # link = container.find('span', class_ ='b07ME mqQL1e').text

data.append({
"Title": title,
"Price": price,
"Supplier": supplier,
# "Link" : link
})

print(json.dumps(data, indent = 2, ensure_ascii = False))