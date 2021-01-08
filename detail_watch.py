import os
import requests
import shutil
import re



def get_price(soul):
    raw_price_product = soul.find("div", {'class': 'price'}).text.split()
    price_product = None
    if raw_price_product != [] and raw_price_product is not None:
        price_product = soul.find("div", {'class': 'price'}).text.split()[1]
    return price_product 

def get_highlight_info(soul):
    div_spec_icons = soul.find('div', {'class': "spec-icons"})
    list_highlight_info = list()
    if div_spec_icons:
        div_columns = div_spec_icons.find_all("div", {"class": "column"})
        for div in div_columns:
            dict_spec_icon = dict()
            dict_spec_icon['spec_icon'] = div.figure.text
            if div.find('div', {"class": "details"}) is None:
                dict_spec_icon['detail_spec_icon'] = None
            else:
                dict_spec_icon['detail_spec_icon'] = div.find(
                    'div', {"class": "details"}).text
            list_highlight_info.append(dict_spec_icon)
    return list_highlight_info


def download_image(soul, name_product):
    div_swiper_wrapper = soul.find('div', {'class': 'swiper-wrapper'})
    list_images_product = list()
    for div in div_swiper_wrapper.find_all('div', {"class": "swiper-slide js-zoom zoom"}):
        list_images_product.append("http:"+div["data-img-narrow"])
    path_product = os.path.join("img", name_product)
    if os.path.exists(path_product) is False:
        os.mkdir(path_product)
        for img in list_images_product:
            filename = img.split('/')[-1]
            path_filename = os.path.join(path_product, filename)
            r = requests.get(url=img, stream=True)
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
                with open(path_filename, 'wb+') as f:
                    shutil.copyfileobj(r.raw, f)
    else:
        return path_product, False
    return path_product, True


def get_introduct_watch(soul):
    introduce_product = None
    if soul.find("div", {"class": "js-cont-wrap"}).p is not None:
        raw_introduce_product = soul.find("div", {"class": "js-cont-wrap"}).p.text
        introduce_product = re.sub(r'\n\s+','',raw_introduce_product)
    elif soul.find("div", {"class": "js-cont-wrap"}).text:
        raw_introduce_product = soul.find("div", {"class": "js-cont-wrap"}).text
        introduce_product = re.sub(r'\n?\s+','',raw_introduce_product)
    return introduce_product

def get_code_watch(soul):
    div_category_products = soul.find("div", {"class": "grid-1 grid-w--1"})
    ol_category_products = div_category_products.find('ol')
    li = ol_category_products.find_all('li')[2]
    code_watch = li.a.text
    return code_watch

def get_list_specification_product(soul):
    list_specification_product = list()
    div_specification_display_list = soul.find('ul', {'class': 'display-list'})
    if div_specification_display_list is not None:
        list_specification = div_specification_display_list.find_all('li')
        for li in list_specification:
            list_specification_product.append(li.text)
    return list_specification_product


def get_color_variations(soul):
    div_color_variation_list = soul.find(
        'section', {'class': 'color-variation-list'})
    list_product_same_color = list()
    if div_color_variation_list:
        list_color_variation_img = div_color_variation_list.find_all(
            'figure', {'class': 'figure'})
        for figure in list_color_variation_img:
            list_product_same_color.append(figure.a['href'])
    return list_product_same_color