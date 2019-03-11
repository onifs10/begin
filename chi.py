from pandas import DataFrame
from requests import get
# from urllib.request import urlopen
from bs4 import BeautifulSoup
r = open("Nairaland Forum.html")
soup = BeautifulSoup(r,'html.parser')
x = soup.find_all('td','homeuser')
for i in x:
    y = i.get_text()
y = y.replace('Birthdays:','').replace('(','-').replace(')','').split(',')
print(y)