from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:\Program Files (x86)\chromedriver')

urlList = ['https://www.flipkart.com/health-care/home-medicines/pr?sid=hlc,ah4&marketplace=FLIPKART',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=3',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=4',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=5',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=6',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=7',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=8',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=9',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=10',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=11',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=12',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=13',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=14',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=15',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=16',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=17',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=18',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=19',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=20',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=21',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=22',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=23',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=24',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=25',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=26',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=27',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=28',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=29',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=30',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=31',
           'https://www.flipkart.com/search?q=medicines&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=32',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc,ah4,wwq&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=5',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=6',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=7',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=8',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=9',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=10',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=11',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=12',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=13',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=14',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=15',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=16',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=17',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&otracker=categorytree&page=18',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=19',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=20',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=21',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=22',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=23',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=24',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=25',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=26',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=27',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=28',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=29',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/pr?sid=hlc%2Cah4%2Cwwq&q=medicines&otracker=categorytree&page=30',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/lens-solutions/pr?sid=hlc,ah4,wwq,n65&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/lens-solutions/pr?sid=hlc%2Cah4%2Cwwq%2Cn65&q=medicines&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/lens-solutions/pr?sid=hlc%2Cah4%2Cwwq%2Cn65&q=medicines&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/lens-solutions/pr?sid=hlc%2Cah4%2Cwwq%2Cn65&q=medicines&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc,ah4,wwq,fvh&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=5',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=6',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=7',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=8',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=9',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=10',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=11',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=12',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=13',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=14',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=15',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=16',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=17',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=18',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=19',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=20',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=21',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=22',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=23',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=24',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=25',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=26',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=27',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=28',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=29',
           'https://www.flipkart.com/health-care/home-medicines/eye-care/contact-lens/pr?sid=hlc%2Cah4%2Cwwq%2Cfvh&q=medicines&otracker=categorytree&page=30',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc,ah4,tfg&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=5',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=6',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=7',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=8',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=9',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=10',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=11',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=12',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=13',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=14',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=15',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=16',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=17',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=18',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=19',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=20',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=21',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=22',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=23',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=24',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=25',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=26',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=27',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=28',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=29',
           'https://www.flipkart.com/health-care/home-medicines/hearing-care/pr?sid=hlc%2Cah4%2Ctfg&q=medicines&otracker=categorytree&page=30',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc,ah4,xos&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=5',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=6',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=7',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=8',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=9',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=10',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=11',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=12',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=13',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=14',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=15',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=16',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=17',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=18',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=19',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=20',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=21',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=22',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=23',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=24',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=25',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=26',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=27',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=29',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=30',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=31',
           'https://www.flipkart.com/health-care/home-medicines/body-pain-relief/pr?sid=hlc%2Cah4%2Cxos&q=medicines&otracker=categorytree&page=32',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc,ah4,iav,raa&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=5',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=6',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=7',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=8',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=9',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=10',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=11',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=12',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=13',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=14',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=15',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=16',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=17',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=18',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=19',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=20',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=21',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=22',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=23',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=24',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=25',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=26',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=27',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=28',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=29',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/homeopathy/pr?sid=hlc%2Cah4%2Ciav%2Craa&q=medicines&otracker=categorytree&page=30',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc,ah4,iav,jnk&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=2',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=3',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=4',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=5',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=6',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=7',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=8',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=9',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=10',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=11',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=12',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=13',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=14',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=15',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=16',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=17',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=18',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=19',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=20',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=21',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=22',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=23',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=24',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=25',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=26',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=27',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=28',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=29',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=30',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=31',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=32',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=33',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=34',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=35',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=36',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=37',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=38',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/ayurvedic/pr?sid=hlc%2Cah4%2Ciav%2Cjnk&q=medicines&otracker=categorytree&page=39',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/allopathy/pr?sid=hlc,ah4,iav,6ym&q=medicines&otracker=categorytree',
           'https://www.flipkart.com/health-care/home-medicines/general-wellness/allopathy/pr?sid=hlc%2Cah4%2Ciav%2C6ym&q=medicines&otracker=categorytree&page=2',
           '']          

product_name = []
product_newPrice = []
product_oldprice = []
quantity = []
stars = []
rating = []
discount = []
description = []


for i in urlList:
    driver.get(i)
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
            product_oldprice.append(old_price.text)
        else:
            product_oldprice.append("0")
        if(new_price!=None):
            product_newPrice.append(new_price.text)
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
            rating.append(rate.text)
        else:
            rating.append("0")
        if(descrip!=None):
            description.append(descrip.text)
        else:
            description.append("Not Available")

    df = pd.DataFrame(
    {"MedicineName":product_name ,"Old price":product_oldprice,"NewPrice":product_newPrice,"Quantity":quantity,"Stars":stars,
      "Rating":rating,"Description":description })
    df.to_csv('newdata.csv',index=False)
              
print(len(product_name),len(product_newPrice),len(product_oldprice))        
for i in range(0,len(product_name)):
    print(product_name[i],product_newPrice[i],product_oldprice[i],quantity[i],stars[i],rating[i],description[i])