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

for row in df.iterrows():
	print(df["Name"])
	break

df2 = df[df["Year"] < 1990]
print(df2)
df3 = df2[df2["Gender"] == "Male"]
df4 = df3[df3["Status"] == "Deceased"]
print(df3)

df5 = df.sort_values("Name", ascending="False")
for name in df2["Name"]:
	print(name)