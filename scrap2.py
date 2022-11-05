from itertools import product
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:\Program Files (x86)\chromedriver')


product_name =[]
product_newPrice = []
product_oldprice =[] 
quantity = []                               
stars = []
rating = []
discount = []
description = []

urlList = ['https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicine&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicine&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/pr?sid=hlc%2Cah4%2Ciav&q=medicine&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/post-natal-care/pr?sid=hlc%2Cah4%2Ced5&q=medicine&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/skin-care/pr?sid=hlc%2Cah4%2Cjn8&q=medicine&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/digestive-health/pr?sid=hlc%2Cah4%2C2bl&q=medicine&otracker=categorytree&page=',
           'https://www.flipkart.com/health-care/home-medicines/hair-care/pr?sid=hlc%2Cah4%2C0tg&q=medicine&otracker=categorytree&page='
           'https://www.flipkart.com/health-care/home-medicines/deficiencies/pr?sid=hlc%2Cah4%2C5i6&q=medicines&otracker=categorytree&page='
           'https://www.flipkart.com/health-care/home-medicines/bone-joint-and-muscle-care/pr?sid=hlc%2Cah4%2Cvv6&q=medicines&otracker=categorytree&page=']
           



for j in urlList:
    for i in range(2,32):
        i = str(i)
        driver.get( j + i)
        content = driver.page_source
        soup = BeautifulSoup(content,"html5lib")
        for name in soup.findAll('div',{'class':'_4ddWXP'}):
            name2 = name.find('a',{'class':'s1Q9rs'})
            old_price = name.find('div',{'class':'_3I9_wc'})
            new_price = name.find('div',{'class':'_30jeq3'})
            quanti = name.find('div',{'class':'_3Djpdu'})
            star = name.find('div',{'class':'_3LWZlK'})
            rate = name.find('span',{'class':'_2_R_DZ'})
            disc = name.find('div',{'class':'_3Ay6Sb'})
            descrip = name.find('div',{'class':'_2Tpdn3 _18hQoS'})
            if(name2!=None):
                product_name.append(name2.text)
            else:
                product_name.append(" ")
            if(old_price!=None):
                product_oldprice.append(old_price.text.replace('₹','').replace(',',''))
            else:
                product_oldprice.append("0")
            if(new_price!=None):
                product_newPrice.append(new_price.text.replace('₹','').replace(',',''))
            else:
                product_newPrice.append("0")
            if(quanti!=None):
                quantity.append(quanti.text)
            else:
                quantity.append("0")
            if(star!=None):
                stars.append(star.text)
            else:
                stars.append("0")
            if(rate!=None):
                rating.append(rate.text.replace('(','').replace(')','').replace(',',''))
            else:
                rating.append("0")
            if(disc!=None):
                discount.append(disc.text)
            else:
                discount.append("0")
            if(descrip!=None):
                description.append(descrip.text)
            else:
                description.append("Not Available")
        print(i)
        df = pd.DataFrame(
        {"MedicineName":product_name ,"Old price":product_oldprice,"NewPrice":product_newPrice,"Quantity":quantity,"Stars":stars,
        "Rating":rating,"Discount": discount,"Description":description })
        df.to_csv('newdata3.csv',mode='a',index=False,header = False)

print(len(product_name),len(product_newPrice),len(product_oldprice))        
for i in range(0,len(product_name)):
    print(product_name[i],product_newPrice[i],product_oldprice[i],quantity[i],stars[i],rating[i],discount[i],description[i])
