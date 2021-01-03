"""
First steps: objects orientation

In this lesson you will learn: 
How to use object orientation in python
How to create a class
What methods are

We have already worked with objects, such as the Python List objject, to which we have applied methods such as the append() method:
"""


students = ["Max", "Monica"]
students.append("Eric")

print(students)

class Student():
	def get_name(self):
		print(self.firstname + " " + self.lastname)

eric = Student()
eric.firstname = "Eric"
eric.lastname = "Miller"
eric.get_name()

monica = Student()
monica.firstname = "Monica"
monica.lastname = "Fisher"

monica.get_name()

class Company():
	def get_name(self):
		print(self.legal_name + " " + self.legal_type)

c = Company()
c.legal_name = "Max Miller"
c.legal_type = "Ltd."
c.get_name()

def name_5x(o): # calling get_name object 
	o.get_name()
	o.get_name()
	o.get_name()
	o.get_name()
	o.get_name()

name_5x(eric) # calling name_5x which calls get_name object x 5
name_5x(c)