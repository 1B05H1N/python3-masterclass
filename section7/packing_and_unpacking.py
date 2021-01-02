"""
Working with tuples

In this lesson you will learn how to ...
use tuples to model multiple return values of a function
unpack tuples
"""

student = ("John Doe", 22, "Informatics")

name = student[0]
age = student[1]
subject = student[2]

print(name)
print(age)
print(subject)

# cool but inefficient 

student = ("John Doe", 22, "Informatics", "USA")

name, age, subject, country = student # python can unpack tuple, but will not work if tuple includes more/less information than wanting to unpack

print(name)
print(age)
print(subject)

# cooler and efficient

def get_student():
	return("John Doe", 22, "Informatics")

name, age, subject = get_student()

print(get_student)
print(name)
print(age)
print(subject)

students = [("Max Miller", 22, "USA"),
			("Monika Fisher", 27, "CA"),
			("Frank Johnson", 23, "AR")
			] # you can have tuples within lists

for name, age, country in students: # how to unpack tuples in a list
	print(name)
	print(age)
	print(country)