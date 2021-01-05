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
		return self.firstname + " Lastname " + self.lastname

class WorkingStudent(Student):
	def __init__(self, firstname, lastname, company):
		super().__init__(firstname,lastname)
		self.company = company

		def name(self):
			return super().name() + " (" + self.company + ")"

"""student = WorkingStudent("John", "Doe", "ABC Company")
student1 = Student("Monica", "Fisher")
print(student.name())
print(student1.name())
"""

students = [ 
	WorkingStudent("Max", "Miller", "ABC Company"),
	Student("Monica", "Fisher"),
	Student("Eric", "Beric"),
	WorkingStudent("Franziska", "Brewer", "Beer Company")
] # polymorphism - store student as a working student or student. This is possible because you can inherit Student

for student in students:
	print(student.name())