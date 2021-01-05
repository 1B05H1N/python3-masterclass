class Student():
	def __init__(self, firstname, surname):
		self.firstname = firstname
		self.surname = surname

	def name(self):
		return self.firstname + " " + self.surname

class WorkingStudent(Student):
	def __init__(self, firstname, surname, company):
		super().__init__(firstname,surname)
		self.company = company

		def name(self):
			return super().name() + " (" + self.company + ")"

w_student = WorkingStudent("John", "Doa", "Evilcorp")
student = Student("Monica", "Miller")

print(type(w_student))
print(type(student))

if type(student) == Student:
	print("This is only for non working students")
if type(w_student) == WorkingStudent:
	print("Only for the working students")

print(isinstance(w_student, WorkingStudent)) #checks if arg 1 is instance of arg 2
print(isinstance(w_student, Student)) #working student is inheriting from student

students = [ 
	WorkingStudent("Max", "Miller", "ABC Company"),
	Student("Monica", "Fisher"),
	Student("Eric", "Beric"),
	WorkingStudent("Franziska", "Brewer", "Beer Company")
]

for student in students:
	if type(student) == WorkingStudent:
		print(student.name())