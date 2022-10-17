import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

title = soup.title
# print(type(title))

