#Pandas Excell Matlab

import pandas as pd 

df = pd.read_excel("Data.xlsx")
df.head()

years = df ["Year"]
sales = df ["Revenue"]

print(years)
print(sales)

import matplotlib.pyplot as plt

plt.plot(years, sales)
plt.show