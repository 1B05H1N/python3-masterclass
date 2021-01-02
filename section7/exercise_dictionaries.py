"""
Task:

Read the ../data/names.csv file and calculate which name was assigned most often in the whole USA.

Tips:

First read the data into a dictionary and count how often each first name occurs.
Analyze the Dictionary and find out the most common first name. 
Note that if you want to add 2 numbers, you may need to convert a string to a number first. 
Write all your code into a cell. 
"""

#with open("C:/Users/account/Documents/github/Learning/content/data/names.csv", "r") as file:
#	for line in file:
#		print(line)
#		break

file = open("C:/Users/account/Documents/github/Learning/content/data/names.csv", "r")

names = {}

for line in file:
	split = line.strip().split(",")
	if split[0] == "Id":
		continue

	name = split[1]
	count = int(split[5])

	if name in names: 
			names[name] = names[name]+count
	else:
		names[name] = count

max_occurences = 0
name = " "

for key, value in names.items():
	if max_occurences < value:
		print(value)
		print(key)
		max_occurences  = value
		name = key

print(name)
print(max_occurences)

"""
Quiz 10

Question 1:

Which name is the most common in the USA?
"""
print("The answer to quiz 10 is " + name +" with a total of " + str(max_occurences) + "!")
