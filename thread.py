import threading
import concurrent.futures
import urllib.request
from  get_info_watch import get_detail_product_watch_casio


def get_urls() :
    with open('context.txt', 'r') as target:
        urls = target.readlines()
    for index ,url in enumerate(urls):
        # if index < 10:
        yield url[:-1]

def load_url(url, timeout):
    print(url)
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()



URLs = list(get_urls())
with concurrent.futures.ThreadPoolExecutor(max_workers=2,) as executor:
    future_to_url = {executor.submit(load_url, url, 10): url for url in URLs}
    for future in future_to_url:
        future.add_done_callback(get_detail_product_watch_casio)


