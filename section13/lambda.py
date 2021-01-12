"""
Sort data

In this lesson you will learn what lambda functions are all about. These are incredibly handy because they are a short notation of how you can pass a function as a parameter.
"""

students = [
	("Max", 3),
	("Monica", 2),
	("Eric", 3),
	("Paula", 1)
]

def student_key(student):
	return student[1]

students.sort(key=student_key)
print(students)


students = [
	("Max", 3),
	("Monica", 2),
	("Eric", 3),
	("Paula", 1)
]

students.sort(key=lambda student: student[1])
print(students)

f = lambda student: student[1]
f(("Max", 1))