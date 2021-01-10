"""
Data Structures in Python
You have already got to know 2 data structures in Python:

Lists: list1 = ["Hello", "World"]
Dictionaries: d = {"Hello": 5, "World": 4}

But there are also others...In this lesson you will get to know set!
"""

my_list = ["Hello", "World"]
my_list.append("Mars")
print(my_list)

my_set = {"Hello", "World"}
my_set.add("Mars")
print(my_set)

if "Mars" in my_set:
	print("Mars is in the set")

text = "Hello World Hello Marks Hello W0r1d"
words = set()
for word in text.split(" "):
	words.add(word)
print(words)
print(len(words))