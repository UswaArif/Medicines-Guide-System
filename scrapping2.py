import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://www.amcal.com.au/vitamins-supplements/multivitamins"
page = requests.get(url)
print(page.content)
