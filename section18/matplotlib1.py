import matplotlib.pyplot as plt 

plt.plot([1,2,3], [4,5,4], color="orange", linestyle="dashed", marker="o", label="Revenue")
plt.legend()
#plt.show()

import pandas as pd 

df = pd.read_excel("Data.xlsx")
df.head()

years = df ["Year"]
sales = df ["Revenue"]

import matplotlib.pyplot as plt

plt.plot(years, sales)
plt.show()