"""
Exceptions in Python
In this lesson you will learn how to: 

"clean up" after an error, and how to enforce this with a "finally".
"""

try:
	file = open("exists.txt", "r")
	print(file)
	print(5/0)

except FileNotFoundError:
	print("File not found")
except ZeroDivisionError:
	print("Don't divide by zero")
finally:
#	file.close()
	print("File was closed")

def do_something():
	with open("exists2.txt", "r") as file:
		print(file)
		print(4/0)
		return "Hello"

do_something()