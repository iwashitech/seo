# -*- coding: utf-8 -*-
"""
"""

import os
import requests
from bs4 import BeautifulSoup
import csv

user_name = os.environ['USERPROFILE'].replace('\\', '/')
for_csv = []
header = ['url', 'title', 'description', 'h1']
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
    ttl = bs.find("title").string
    desc = bs.find('meta', attrs={'name': 'description'})['content']
    h1 = bs.find("h1").string
    
    result_list.extend([ttl, desc, h1])
    for_csv.append(result_list)
    
with open(user_name + '/Desktop/result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(for_csv)