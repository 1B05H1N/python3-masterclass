"""
Object Orientation: Private Properties and Methods

In this lesson you will learn: 

What private characteristics are...
What private methods are...
...and where / for what you should use them
"""

class Student():

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.__term = 1 # we made term private by using 2 underscores

	def increase_term(self):
		if self.__term >= 9:
			return
		self.__term = self.__term + 1

	def get_term(self):
		self.__do_something()
		return self.__term

	def name(self):
		print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

	def __do_something(self):
		print("doSomething")

eric = Student("Eric", "Johnson")
eric.increase_term()
#eric.__term = 100
#print(eric.__term)
print(eric.get_term())
#eric.__do_something()
eric.name()