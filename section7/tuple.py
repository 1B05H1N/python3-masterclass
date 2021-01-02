"""
Tuple
Tuples are something like a list ... but are used for other purposes. 

This is about what tuples are,....
how they differ from a list
and how to use them in Python
"""


t = (1,2,3) # tuples use () , dictionaries use {} and lists use []
print(t)
# tuples are immutable, and cannot be changed

list1 = [1,2,3]
list1.append(5)
print(list1)

# Excursus Computer Science: Mutable (mutable) vs. Immutable (unchangeable)

person = ["Max Muller", 55]

def do_something(p):
	p[0] = "Max Mustermann" #change argument to Max Mustermann

do_something(person)

print(person)

person = ("Max Muller", 55)

def do_something(p):
	p[0] = "Max Mustermann" #change argument to Max Mustermann

do_something(person) # tuple is not mutable and cannot be changed 

print(person)