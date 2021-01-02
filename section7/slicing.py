students = ["Max", "Monika", "Erik", "Franzsika"]
print(students[-1])
print(students[-2])

## list slicing 

print(students[2:4]) # create temp list
less_students = students[1:3]
print(less_students)

print(students[0:-3])

# slicing works with strings

print("Hello world"[0:5]) # gives me the first 5 chars
print("Hello world"[-5:]) # gives me the last 5 chars

print("Hello world!"[6:-1])