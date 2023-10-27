# -*- coding: utf-8 -*-
"""
"""

import os
from urllib.parse import parse_qsl
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import get as GET

from time import sleep
import codecs

user_name = os.environ['USERPROFILE'].replace('\\', '/')
result = []

items_file = codecs.open(user_name + '/Desktop/items.txt', 'r', 'utf-8')
items_file_list = items_file.readlines()
item_list = [item.replace('\n', '') for item in items_file_list]

for item in item_list:
    html = GET("https://www.google.co.jp/search?q=" + item).text
    bs = BeautifulSoup(html, 'lxml')
    sleep(5)
    
    for el in bs.select("h3.r a"):
        title = el.get_text()
        url = dict(parse_qsl(urlparse(el.get("href")).query))["q"]
        if "example" in url:
            result.append(title + "  " + url)
            break

f = open(user_name + '/Desktop/google_search.txt', 'w')
for x in result:
    f.write(str(x) + "\n")
f.close()