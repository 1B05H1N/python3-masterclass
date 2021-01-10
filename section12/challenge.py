# Task: Sets

import csv

names = set() #set called names 

with open("C:/Users/account/Documents/github/Learning/content/data", newline='') as csvfile:
	namereader = csv.reader(csvfile, delimiter=',', quotechar='"') #create reader
	counter = 0
	for row in namereader:
		if counter != 0:
			names.add(row[1])
		counter = counter +1

print(len(names))

#30274