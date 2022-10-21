# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:40:09 2022

@author: gcaer
"""

import requests
import pandas as pd
from datetime import datetime

url = "https://emodnet.ec.europa.eu/geonetwork/emodnet/eng/q"

querystring = {"_content_type":"json","bucket":"s101","facet.q":"","fast":"index","from":"1","resultType":"details","sortBy":"sortDate","sortOrder":"","to":"20"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "eng",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://emodnet.ec.europa.eu/geonetwork/emodnet/eng/catalog.search",
    "X-XSRF-TOKEN": "73fe47a5-25e6-4ecb-9412-e8df788d784e",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "JSESSIONID=2C06B751EE13628DD584C2120ABDE4C7; XSRF-TOKEN=73fe47a5-25e6-4ecb-9412-e8df788d784e; vliz_webc=vliz_webc1; cck1=%7B%22cm%22%3Afalse%2C%22all1st%22%3Afalse%2C%22closed%22%3Afalse%7D",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

dic = {'date':[],
       'catalog':[],
       'count':[]}

for i in range(2,5):
    catalog = data['summary']['dimension'][6]['category'][i]['@label']
    count = data['summary']['dimension'][6]['category'][i]['@count']
    
    datenow = datetime.today().strftime("%d/%m/%y %H:%M:%S")
    dic['date'].append(datenow)
    dic['catalog'].append(catalog)
    dic['count'].append(count)
    
df = pd.DataFrame(dic)
df.to_csv('result.csv', mode='a', index=False, header=False)

