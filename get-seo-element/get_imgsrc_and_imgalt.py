# -*- coding: utf-8 -*-
"""
"""

import os
import requests
from bs4 import BeautifulSoup
import csv

user_name = os.environ['USERPROFILE'].replace('\\', '/')
for_csv = []
header = ['url', 'img']
for_csv.append(header)

with open(user_name + '/Desktop/list.txt') as f:
    url_list = f.readlines()

for raw_url in url_list:
    result_list = []
    
    url = raw_url.replace('\n', '')
    result_list.append(url)
    response = requests.get(url)
    response.status_code
    
    bs = BeautifulSoup(response.content,"lxml")
    images = bs.find("div", class_="hoge")
    img_list = images.find_all("img")
    
    for img in img_list:
        result_list.append(img['src'])
        result_list.append(img['alt'])
    
    for_csv.append(result_list)
    
with open(user_name + '/Desktop/result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(for_csv)
