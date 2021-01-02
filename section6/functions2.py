# functions with multiple parameters and the return function

def multi_print(name, count):
	for i in range(0, count):
		print(name)

multi_print("Denis", 10)

def another_function():
	multi_print("Hello", 3)
	multi_print("World", 3)

another_function()

def maximum(a, b):
	if a < b:
		return b
	else:
		return a

result = maximum(1337, 2018)
print(result)