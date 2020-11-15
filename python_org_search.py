from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import requests
import json

#launch url
url = "https://www.casio.com/products/watches/baby-g"
# url = "https://www.casio.com/products/watches/baby-g/ba112-1a"
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
    list_links.append("https://www.casio.com" + link)

reponse = requests.get(list_links[0])
print(reponse.content)
driver.close()


