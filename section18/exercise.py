name = "Anna"
gender = "F"
state = "CA"

import pandas as pd

df = pd.read_csv("C:/Users/account/Documents/github/Learning/content/data/names.csv")
df.head

df2 = df[df["Name"] == name]
df3 = df2[df2["Gender"] ==  gender]
df4 = df3[df3["State"] == state]
df5 = df4.sort_values("Year")

import matplotlib.pyplot as plt

plt.plot(df5["Year"], df5["Count"])
plt.show()