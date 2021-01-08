import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import json
from get_info_watch import get_detail_product_watch_casio
from threading import Thread

PATH = "C:\Program Files (x86)\chromedriver.exe"

#launch url
# url = "https://www.casio.com/products/watches/baby-g"
# url = "https://www.casio.com/products/watches/g-shock"
url = "https://www.casio.com/products/watches/g-shock-women"
# # create a new Firefox session
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
div_content_body = soup.find('div',{'class':'contents-body'})

div_products = div_content_body.find_all("div",{'class':"info bg-white"})
with open('context.txt', 'w+') as f:
   for div in div_products:
       f.write("https://www.casio.com"+div.a['href']+"\n")

# with open('context.txt', 'r+') as f:
#     links_product = f.read()
# list_links = list()

# for link in links_product.split('\n'):
#     if link is not "":
#         # list_links.append("https://www.casio.com" + link)
#         url = "https://www.casio.com" + link
#         print(url)
#         # list_links.append(get_detail_product_watch_casio(url))

# with open('g-shock.json', 'w+') as target:
#     target.write(json.dumps(list_links))

print("done")
driver.close()


