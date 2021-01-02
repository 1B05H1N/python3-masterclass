print("hello world") # we are calling the print function and passing an argument called hello world

def multi_print(): # defining a new function with the def function
		print("hello World")
		print("hello World")
multi_print() # we're calling the function

multi_print()

def multi_print2(name): # parameter is called name
	print(name)
	print("my name is " + name)
multi_print2("Denis")
# multi_print("Denis") # will generate type error since there are no parameters in the function / it will not take an argument
multi_print2("Frank")

"""
saves time, very powerful, etc
"""