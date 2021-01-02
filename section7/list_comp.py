"""
List comprehensions 

in this lesson you will learn how to 

list comprehensions
how it makes it easier to convert lists into a new list
and we use a list comprehension to make it easier to draw a graphic
"""

xs = [1,2,3,4,5,6,7,8]

ys = []
for x in xs: # for every x value in xs list do the following 
	ys.append(x*x) # append x * x to ys list

print(xs)
print(ys)

ys = [x * x for x in xs] # do something for every element and then for every item do this list

print(xs)
print(ys)

students = ["Max", "Monika", "Erik", "Franziska"]

lengths = []
for student in students:
	lengths.append(len(student))

print(lengths)

lengths = [len(student) for student in students] # length of student for student in students
print(lengths)

# %matplotlib inline

# import matplotlib.pyplot as pyplot

xs = [x / 10 for x in range(0,100)]
ys = [x * x for x in xs] 
print(xs)
#plt.plot(xs, ys)
#ply.show