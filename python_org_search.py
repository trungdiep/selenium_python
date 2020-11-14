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

#After opening the url above, Selenium clicks the specific agency link
# python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
# python_button.click() #click fhsu link

#Selenium hands the page source to Beautiful Soup
# python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
# python_button.click() #click fhsu link
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
for div in soup.select('.info ,.bg-white'):
    u = "https://www.casio.com/"+div.a['href']
    # dri.get(u)
    r = requests.get(url=u)
    s = BeautifulSoup(r.content,"html.parser")

    # html_source = html = dri.page_source
    # print(html_source)
    print(s.title)

driver.close()


