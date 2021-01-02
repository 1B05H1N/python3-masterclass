students = ["Max", "Monika", "Erik", "Fransizka"]

last_student = students.pop()
print(last_student)
print(students)

students = ["Max", "Monika", "Erik", "Fransizka"] + ["Frank"] + ["Rodrigo"]
print(students)

del students[3] # using del
print(students)

students.remove("Monika") # remove method usage
print(students)

students.remove("Rodrigo")
print(students)

