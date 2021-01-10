import requests
import json
from bs4 import BeautifulSoup
import shutil  # to save it locally
import os
from concurrent import futures
from detail_watch import(get_price, get_highlight_info, download_image, get_introduct_watch,
                         get_code_watch, get_list_specification_product, get_color_variations)
from database.connect import connect

# url_product = "https://www.casio.com/products/watches/baby-g/bg169m-4"
# url_product = "https://www.casio.com/products/watches/g-shock-women/msgs500g-1a"



def get_detail_product_watch_casio(fut: futures):
    context_request = fut.result()
    soul = BeautifulSoup(context_request, 'html.parser')
    
    url_product = soul.find("meta",{"property":"og:url"})["content"]

    #name watch
    div_name = soul.find("div", {'class': 'name'})
    name_product = div_name.h2.text

    # get gia
    price_product = get_price(soul)

    # ? new
    new_product = False
    if soul.find("mark") is not None:
        new_product = True

    # cac thong tin noi bat cua dong ho
    list_highlight_info = get_highlight_info(soul)

    # anh dong ho
    check_download = download_image(soul, name_product)
    if check_download[1] == False:
        return
    else:
        path_image_product = check_download[0]

    # introduct watch
    introduct_watch = get_introduct_watch(soul)

    # code watch
    code_watch = get_code_watch(soul)

    # list specification watch
    list_specification_product = get_list_specification_product(soul)

    # various color
    list_product_same_color = get_color_variations(soul)

    dict_product = dict()
    dict_product["category_product"] = code_watch
    dict_product["introduce_product"] = introduct_watch
    dict_product["list_spec_icon"] = list_highlight_info
    dict_product["price_product"] = price_product
    dict_product["name_product"] = name_product
    dict_product["url_product"] = url_product
    dict_product["list_specification_product"] = list_specification_product
    dict_product["list_product_together_color"] = list_product_same_color
    dict_product["new_product"] = new_product
    dict_product["path_image"] = path_image_product

    print(dict_product)
    # list_product_crawl = get_list_product_crawl(dict_product)

    connect(dict_product)