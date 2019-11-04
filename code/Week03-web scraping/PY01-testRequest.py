import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-------------------")
print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print (soup1.prettify())

