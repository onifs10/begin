import pandas 
from bs4 import BeautifulSoup
r = open('Nairaland Forum.html')
soup = BeautifulSoup(r, 'html.parser')



x = soup.find_all("td","homeuser")
for i in x:
    y = i.get_text()
a = y.replace('Birthdays:',"" ).replace('(',"-").replace(')',"").split(",")

list_ = []
for i in a:
    if "-" in i:
        a = i.split("-")
        list_.extend(a)
    else:
        nop = i + "-0"
        a = nop.split("-")
        list_.extend(a)

user = list_[::2]
age = list_[1::2]

data = pandas.DataFrame({"name":user,"age":age})
data.to_html('age.html')
print(data)
x = open('new_data.csv')
x = pandas.read_csv(x)
print(x)
print(x.plot(kind='pie'))