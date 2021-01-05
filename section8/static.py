"""
Static variables

We can also bind variables to classes instead of instances. They are called static because they are no longer attached to a single instance, but to all instance:
"""

class Car:
	price = "expensive"

c = Car
print(c.price)
bobbycar = Car
print(bobbycar.price)

c.price = "cheap"
print(c.price)
bobbycar = Car
print(bobbycar.price)

bobbycar = Car
print(bobbycar.price)

class CarI:
	color = "blue"
	def __init__(self, price):
		self.price = price

c = CarI("jo")
print(c.price)
print(c.color)

d = CarI("bo")
print(d.price)
print(d.color)