file = open("write.txt", "a") # w for write and a for append

"""
file.write("random text, just like that\n")
file.write("random text, just like that")
file.close()
"""
students = ["Max", "Monika", "Erik", "Franziska"]

for student in students:
	file.write(student + "\n")

file.close()