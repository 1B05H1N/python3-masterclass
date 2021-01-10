"""
How are function parameters passed in Python? 

Python distinguishes between 2 different types of variables: 

Primitive data types (number, string, booleans, ...)
Data Structures / Data Structure
"""
a = 5

def f(x):
	x = 3
	print(x)

f(a)
print(a)

l = ["Hello", "World"]

def f(x):
	x.append("!!!")
	print(x)

f(l)
print(l)

l = ["Hello", "World"]

def f(x):
	x = x.copy()
	print(x)
	x.append(x)
	print(x)
	x = ["Hello", "World", "!!!"]
	print(x)

f(l)
print(l)

