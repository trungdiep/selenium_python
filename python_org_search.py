from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import requests
import json
import asyncio
from bs4_canio_case1 import get_detail_product_watch_casio

#launch url
url = "https://www.casio.com/products/watches/baby-g"
# url = "https://www.casio.com/products/watches/g-shock"
# # create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

dri = webdriver.Firefox()
dri.implicitly_wait(30)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
div_content_body = soup.find('div',{'class':'contents-body'})

div_products = div_content_body.find_all("div",{'class':"info bg-white"})
with open('context.html', 'w+') as f:
   for div in div_products:
       f.write(div.a['href']+"\n")

with open('context.html', 'r+') as f:
    links_product = f.read()
list_links = list()

for link in links_product.split('\n'):
    if link is not "":
        # list_links.append("https://www.casio.com" + link)
        url = "https://www.casio.com" + link
        print(url)
        list_links.append(get_detail_product_watch_casio(url))

with open('g-shock.json', 'w+') as target:
    target.write(json.dumps(list_links))

print("done")
driver.close()


