"""
Passive variable function parameters
"""

def f(a,b,c):
	print(a)
	print(b)
	print(c)

l = [1,2,3]
f(l[0], l[1], l[2])

f(*l) # use elements in list as arguments

def calculate_max(current_max, *params): # wildcard indicates flexible amount of params
	print(current_max)
	print(params)
	current_max = params[0]
	for item in params:
		if item > current_max:
			current_max = item
	return current_max

calculate_max(1,2,3,4,123412,1234,1243,1234)