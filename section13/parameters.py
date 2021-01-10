"""
Name function parameters

Sometimes you work with a function that gets a lot of parameters. Then the function call quickly becomes very confusing...

In this lesson you will learn: 

What default parameters are
How to pass named parameters to a function.

"""

def multi_print(number, word):
	for i in range(0, number):
		print(word)

multi_print(5, "Hello")

def multi_print(number = 3, word = "Words"):
	for i in range(0, number):
		print(word)

multi_print()

def multi_print(number = 3, word = "Six"):
	for i in range(0, number):
		print(word)

multi_print(6)

def multi_print(number = 3, word = "Seven"):
	for i in range(0, number):
		print(word)

multi_print(word = "Eight", number = 8)