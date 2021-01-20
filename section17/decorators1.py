def outer(func):
	cached = {}
	def inner(x):
		if x in cached:
			return cached[x]
		result = func(x)
		cached[x] = result
		return func(x)

	return inner

@outer
def calculate_something(x):
	print("calculate_something(" + str(x) + ")")
	#couldn't get the return x * x to work due to syntax error
	sum = x * x
	return sum

print(calculate_something(5))
print(calculate_something(5))