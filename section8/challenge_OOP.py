"""
Challenge: Object Orientation

Now take a look at the exercise sheet on object orientation and work on the tasks given there.

You can find this exercise sheet in the course materials you downloaded in the first section. It is located in the folder "08 - Object Orientation", the file is called "Exercise - Object Oriented Programming".

Have fun with the tasks :)

Exercise: Object-oriented programming

Attached you will find some tasks for programming. Have fun with it! :)

When you have finished this exercise sheet, compare it with the sample solution.

The video sample solution (in the next lesson) is explained in details. If you have solved everything correctly, it is perfectly okay if you skip this lesson then.

Task 1: Model a cube

Create a class Cube to model a cube! The cube class should have the length of the cubes side as a property. In addition, the class should have two methods: the method volume() calculates the volume and outputs it, the method surface() calculates the surface and outputs it.
"""

class Cube():
    # Your code here
    def __init__(self, side): # parameterized constructor 
    	self.side = side

    def surface(self): 
    	print(self.side ** 2 * 6)

    def volume(self):
    	print(self.side ** 3)

# instance of your Cube-class 
a = Cube(3)

# test of the class
a.surface()
a.volume()

"""
Task 2: Model a sphere

The Ball class should be given the radius as a property. It should also have two methods - similar to the cube: surface() to calculate the surface content, volume() to calculate the volume.

In order to perform these calculations, you need the circle number Pi. This is available to you after an import math under math.pi (what the import command exactly does, we will look at later in the course).

You can look up the formulas for the surface content/volume of a sphere on the Internet.
"""

import math
print(math.pi)

import math

class Ball():

	def __init__(self, radius):
		self.radius = radius

	def surface(self):
		print(4 * math.pi * self.radius * self.radius)

	def volume(self):
		print(4 / 3 * math.pi * self.radius ** 3)

b = Ball(4)

b.surface()
b.volume()

"""
Task 3: Model an account
a.)

Create the class Account with the property credits! This property is initialized with a starting capital. The method display() should display the current account balance.
"""

class Account():

	def __init__(self, start):
		self.credits = start

	def display(self):
		print(self.credits)

Customer = Account(500)
Customer.display()

"""
b.)

Add two methods (pay_in() to deposit, withdraw() to withdraw) to the Account class so that you can deposit and withdraw funds, and the account balance will be adjusted accordingly.

I just want you to be able to withdraw money while there's money in your account. You can't go into debts. In this case, an error message should be issued stating the maximum amount of money that can be accessed.
"""
class Account():

	def __init__(self, start):
		self.credits = start

	def display(self):
		print(self.credits)

	def pay_in(self, money):
		self.credits += money

	def withdraw(self, money):
		if self.credits >= money:
			self.credits -= money
		else: 
			print("Insufficient funds. Your broke ass only has $" + str(self.credits) + "!!!")		

Customer = Account(500)
Customer.display()
Customer.pay_in(500)
Customer.display()
Customer.withdraw(50)
Customer.display()
Customer.withdraw(2000)
Customer.pay_in(200000)
Customer.display()
Customer.withdraw(1000)
Customer.display()

"""
c.)

The account is still unprotected - we need a PIN! In the class, add the property pin! As with the initial capital, the account should also be initialized with a PIN.

From now on you have to enter not only the amount but also the PIN when you withdraw money: Only if the PIN matches the PIN of the account, money can be withdrawn, otherwise an error message will be displayed!
"""

class Account():

	def __init__(self, start, pin):
		self.credits = start
		self.pin = pin

	def display(self):
		print(self.credits)

	def pay_in(self, money):
		self.credits += money

	def withdraw(self, money, pin):
		if pin == self.pin:
			if self.credits > money:
				self.credits -= money
			else: 
				print("Insufficient funds. Your broke ass only has $" + str(self.credits) + "!!!")
		else:
			print("Wrong PIN !!!")		

Customer = Account(500, "187")
Customer.display()
Customer.pay_in(500)
Customer.display()
Customer.withdraw(50, "187")
Customer.display()
Customer.withdraw(2000, "187")
Customer.pay_in(200000)
Customer.display()
Customer.withdraw(1000, "1831247")
Customer.display()

"""
Task 4: Model a train

a.)

Now you will build train objects! Create the class Train, which is initialized with the properties route and position! route is a list of the train's stations. position stands for the index of the station from the list from which the train is currently or last departed (where exactly the train is on the line between two stations is of no interest to us here). With the method show_station() the name of this station should be output.
"""

class Train():

	def __init__(self, route, start):
		self.route = route
		self.position = start

	def show_station(self):
		print(self.route[self.position])

orientexpress = Train(["Paris", "Budapest", "Bucharest", "Istanbul"], 0)
orientexpress.show_station()

"""
b.)

So far, a train of the class Train is still stuck in its starting station. Now add two methods move() and move_back() to move a train on its route to the next or previous station. The train must not leave its route!
"""

class Train():

	def __init__(self, route, start):
		self.route = route
		self.position = start

	def show_station(self):
		print(self.route[self.position])

	def move(self):
		if self.position < len(self.route) - 1:
			self.position +=1
		else:
			print("Final Stop!")

	def move_back(self):
		if self.position > 0:
			self.position -= 1

orientexpress = Train(["Paris", "Budapest", "Bucharest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move_back()
orientexpress.show_station()
orientexpress.move_back()
orientexpress.show_station()
orientexpress.show_station()
orientexpress.move_back()
orientexpress.show_station()
orientexpress.move_back()

"""
c.)

It should be possible to edit the route later by using a bypass_station(), which makes the train leave it's route. To be on the safe side, the train should then be moved to the start of the route, unless it is already there.

Tip:*** Remember the methods for lists! :-)
"""

class Train():

	def __init__(self, route, start):
		self.route = route
		self.position = start

	def show_station(self):
		print(self.route[self.position])

	def move(self):
		if self.position < len(self.route) - 1:
			self.position +=1
		else:
			print("Final Stop!")

	def move_back(self):
		if self.position > 0:
			self.position -= 1

	def bypass(self, station):
		if station in self.route:
			self.route.remove(station)
			self.position = 0

orientexpress = Train(["Paris", "Budapest", "Bucharest", "Istanbul"], 0)
orientexpress.bypass("Budapest")
orientexpress.move()
orientexpress.show_station()