"""
In Python everything is an onject

numbers are objects
Let's apply the type() function to variables in which we have stored numbers:
"""

a = 13

print(type(a))

b = 12.5
print(type(b))

a.__add__(5)

15+13

a.__sub__(5)

a.__mul__(5)

(12.5).__truediv__(6.25)

s = "Hello World"
print(type(s))

len(s)

s.__len__() #what's done internally 

class A:
	def __len__(self):
		return 6

instance = A()
len(instance)
instance.__len__()