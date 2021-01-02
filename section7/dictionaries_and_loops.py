"""
Dictionaries and loops

In this lesson you will learn:

How to go through a Dictionary entry by entry:
And why you need to unpack tuples for it :)
"""

d = {"Munich": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}

for key in d:
	value = d[key] # gets entry for he key and gets the value
	print(key)

print(d.items())

for key, value in d.items(): # unpacking of tuples and for loop to go through tuples 
	print(key + ": " + value)