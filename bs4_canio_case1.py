import requests
import json
from bs4 import BeautifulSoup
import shutil # to save it locally
import os



url_product = "https://www.casio.com/products/watches/baby-g/bg169m-4"

def get_detail_product_watch_casio(url_product):
    r = requests.get(url=url_product)

    soul = BeautifulSoup(r.content,'html.parser')
    div_name = soul.find("div",{'class':'name'})
    name_product = div_name.h2.text
    # price_product = soul.find("div",{'class':'price'}).text.split()[1]
    if os.path.exists(name_product+'.json'):
        return
    raw_price_product = soul.find("div",{'class':'price'}).text.split()

    price_product = None
    if raw_price_product != [] and raw_price_product is not None:
        price_product = soul.find("div",{'class':'price'}).text.split()[1]

    div_spec_icons = soul.find('div',{'class':"spec-icons"})
    list_spec_icon = list()
    if div_spec_icons:
        div_columns = div_spec_icons.find_all("div",{"class":"column"})
        for div in div_columns:
            dict_spec_icon = dict()
            dict_spec_icon['spec_icon'] = div.figure.text
            if div.find('div',{"class":"details"}) is None:
                dict_spec_icon['detail_spec_icon'] =  None
            else:
                dict_spec_icon['detail_spec_icon'] =  div.find('div',{"class":"details"}).text
            list_spec_icon.append(dict_spec_icon)



    div_swiper_wrapper = soul.find('div',{'class':'swiper-wrapper'})
    list_imgs_product = list()
    for div in div_swiper_wrapper.find_all('div'):
        list_imgs_product.append("http:"+div["data-img-narrow"])

    path_product = os.path.join("img",name_product)
    if os.path.exists(path_product) is False:
        os.mkdir(path_product)

        for img in list_imgs_product:
            filename = img.split('/')[-1]
            path_filename = os.path.join(path_product,filename)
            r = requests.get(url=img, stream=True)
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
                with open(path_filename,'wb+') as f:
                    shutil.copyfileobj(r.raw, f)

    introduce_product = soul.find("div",{"class":"js-cont-wrap"}).p.text
    dict_product = dict()

    div_category_products = soul.find("div",{"class":"grid-1 grid-w--1"})
    ol_category_products = div_category_products.find('ol')
    li = ol_category_products.find_all('li')[2]
    # print(div_category_products)
    category_product = li.a.text


    # div_specification = soul.find('div',{'class':'grid-1 grid-n--1 frame'})
    list_specification_product = list()
    div_specification_display_list = soul.find('ul',{'class':'display-list'})
    if div_specification_display_list is not None:
        list_specification = div_specification_display_list.find_all('li')
        for li in list_specification:
            list_specification_product.append(li.text)

    div_color_variation_list = soul.find('section',{'class':'color-variation-list'})
    list_product_together_color = list()
    if div_color_variation_list:
        list_color_variation_img = div_color_variation_list.find_all('figure',{'class':'figure'})

        for figure in list_color_variation_img:
            list_product_together_color.append(figure.a['href'])

        # print(list_product_together_color)

    dict_product["category_product"] = category_product
    dict_product["introduce_product"] = introduce_product
    dict_product["list_spec_icon"] = list_spec_icon
    dict_product["price_product"] = price_product
    dict_product["name_product"] = name_product
    dict_product["url_product"] = url_product
    dict_product["list_specification_product"] = list_specification_product
    dict_product["list_product_together_color"] = list_product_together_color
    with open(name_product+".json",'w+') as target:
        target.write(json.dumps(dict_product))


get_detail_product_watch_casio(url_product)