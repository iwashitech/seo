# -*- coding: utf-8 -*-
"""
"""

import os
import requests
from bs4 import BeautifulSoup
import csv

user_name = os.environ['USERPROFILE'].replace('\\', '/')
for_csv = []
header = ['url', 'breadcrumbs']
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
    breadcrumbs = bs.find("ul", class_="breadcrumbs")
    bc_list = breadcrumbs.find_all("li")
    
    for bc in bc_list:
        result_list.append(bc.string)
        if bc.find('a'):
            result_list.append(bc.find('a')['href'])
    
    for_csv.append(result_list)
    
with open(user_name + '/Desktop/result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(for_csv)