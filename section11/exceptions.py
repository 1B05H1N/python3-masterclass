"""
Exceptions in Python

In this lesson you will learn how to deal with an error if one occurs during the runtime of your program. 
"""
"""x = 0
print(5/x)

with open("file.xyz", "r") as file:
	print(file)"""

try: 
	print(5/0)
	print(4)
except ZeroDivisionError:
	print("Do not divide by zero")
print(5)

try:
	with open("file.xyz", "r") as file:
		print(file)
except FileNotFoundError:
	print("File not found")