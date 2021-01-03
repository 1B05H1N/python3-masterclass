"""
Inheritance

Inheritance is a fundamental concept of object orientation with which you can divide and better model data. 

We already know the class student:
"""

class Student():
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.term = 1

	def name(self):
		return self.firstname + " lastname " + self. lastname

class WorkingStudent(Student):
	def __init__(self, firstname, lastname, company):
		super().__init__(firstname,lastname)
		self.company = company

		def name(self):
			return super().name() + " (" + self.company + ")"

student = WorkingStudent("John", "Doe", "ABC Company")
student1 = student("Monica", "Fisher")
print(student.name())
print(student1.name())

