# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 05:48:29 2022

@author: HP
"""

import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv

header = {'Origin': 'https://www.flipkart.com/',
          'Referer':'https://www.flipkart.com/health-care/home-medicines/pr?sid=hlc,ah4&marketplace=FLIPKART',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
         }

url = 'https://www.flipkart.com/health-care/home-medicines/pr?sid=hlc,ah4&marketplace=FLIPKART'

html = requests.get(url=url,headers=header)
bsobj = soup(html.content,'lxml')
#print(bsobj.find_all('script type="text/javascript"'))
#print(bsobj)

product_name = []
product_newPrice = []
product_oldprice = []
quantity = []
stars = []
rating = []
discount = []
description = []


for name in bsobj.findAll('a',{'class':'s1Q9rs'}):
    product_name.append(name.text.strip())
    
for name in bsobj.findAll('div',{'class':'_30jeq3'}):
    product_newPrice.append(name.text.strip())
    
for name in bsobj.findAll('div',{'class':'_3I9_wc'}):
    product_oldprice.append(name.text.strip())

for name in bsobj.findAll('div',{'class':'_3Djpdu'}):
    quantity.append(name.text.strip())
  
for name in bsobj.findAll('div',{'class':'_3LWZlK'}):
    stars.append(name.text.strip())
    
for name in bsobj.findAll('span',{'class':'_2_R_DZ'}):
    rating.append(name.text.strip())    

for name in bsobj.findAll('div',{'class':'_3Ay6Sb'}):
    discount.append(name.text.strip())    
    
for name in bsobj.findAll('div',{'class':'_2Tpdn3 _18hQoS'}):
    description.append(name.text.strip())  
 

lists = bsobj.findAll('div',{'class':'_36fx1h _6t1WkM _3HqJxg'})
for list in lists:
    name = list.find('a',class_ = 's1Q9rs')
    info = [name]
    print(info)

print(product_name)
print(product_newPrice)
print(product_oldprice)
print(quantity)
print(stars)
print(rating)
print(discount)
print(description)


    


