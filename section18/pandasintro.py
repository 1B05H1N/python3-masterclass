#Pandas: Read in tabular data

# With pandas, we can import CSV/Excel files and thens sort/filter them

import pandas as pd 
df = pd.read_csv("C:/Users/account/Documents/github/Learning/content/data/astronauts.csv", delimiter=",")
df.head()
print(df.head())

a = len(df)
print(a)

for name in df["Name"]:
	print(name)

df.iloc[0]
print(df.iloc[0])

entry = df.iloc[0]
print(entry["Name"])
print(entry["Year"])
print(entry["Birth Date"])

df.iloc[4:8]
print(df.iloc[4:8])
print(df.iloc[-5:])
