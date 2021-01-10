"""
Exceptions in Python
In this lesson you will learn how to:

"clean up" after an error, and how to correctly enforce this with a "finally".
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
	file.close()
	print("File was closed")
