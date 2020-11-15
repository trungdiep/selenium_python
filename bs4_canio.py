import requests
import json
from bs4 import BeautifulSoup



url_product = "https://www.casio.com/products/watches/baby-g/bgd560s-8"

r = requests.get(url=url_product)
soul = BeautifulSoup(r.content,'html.parser')
div_name = soul.find("div",{'class':'name'})
name_product = div_name.h2.text
price_product_raw = soul.find("div",{'class':'price'}).text.split()[1]
div_spec_icons = soul.find('div',{'class':"spec-icons"})
div_columns = div_spec_icons.find_all("div",{"class":"column"})
list_spec = list()
for div in div_columns:
    list_spec.append(div.figure.text)

div_swiper_wrapper = soul.find('div',{'class':'swiper-wrapper'})
list_imgs_product = list()
for div in div_swiper_wrapper.find_all('div'):
    list_imgs_product.append(div["data-img-narrow"][2:])

print(list_imgs_product)

print(list_spec)
print(price_product_raw)
print(name_product)