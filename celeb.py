from urllib.request import urlopen
from bs4 import BeautifulSoup
x= urlopen('https://www.nairaland.com/')
print(x)
soup =  BeautifulSoup(x,'html.parser')
print(soup)