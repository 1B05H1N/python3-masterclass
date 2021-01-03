"""
Object orientation: constructor, change properties

In this lesson you will learn how to: 
Use a constructor to define the properties of a class
Change the properties of an instance. 

We have already extended the Student class a litle:
"""

class Student():

	def __init__(self, firstname, lastname, term): # 2 underscores init and 2 underscores

		self.firstname = firstname
		self.lastname = lastname
		self.term = term

	def increase_term(self):
		self.term = self.term + 1 

	def get_name(self):
		print(self.firstname + " " + self.lastname + " Semester is " + str(self.term))

eric = Student("Eric", "Miller", 2)
eric.increase_term()
eric.get_name()

monica = Student("Monica", "Fisher", 5)
monica.get_name()


