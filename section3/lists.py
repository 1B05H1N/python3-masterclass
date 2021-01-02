# inefficient way of creating a list
student1 = "Max"
student2 = "Monika"
student3 = "Erik"
student4 = "Franziska"

# list containing student names stored as strings
students = ["Max" , "Monika" , "Erik" , "Franziska"]
print(students)

marks = [4, 3, 2, 1]
print(student1)

# to call "Max" we reference the variable and the index for "Max" (he's at position 0)
print(students[0])

# same as before, but we are calling "Erick". Erick is the 2nd index.
print(students[2])

# call Max and Franziska
print(students[0] + " & " + students[3])

# if you want to know how many values are in a list you can use the length function "len"
print(len(students))

# the append function can be used to append or add something to a list 
students.append("Moritz")
print(len(students))

print(students)

# appending Moritz grade to the marks list
marks.append(2)
print(len(marks))

# average grades for all students including Moritz 
print((marks[0] + marks[1] + marks[3] + marks[4] + marks[4]) / len(marks))
