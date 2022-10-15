from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.amcal.com.au/vitamins-supplements/multivitamins")
print("Manoor")