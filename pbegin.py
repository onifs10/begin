import pandas as pd
x = open('new_data.csv')
x = pd.read_csv(x)
import matplotlib
print(x.head(10).plot(kind='pie', x='Total Cost' , y = 'Total Revenue'))