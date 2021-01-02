"""
Nesting lists

In Python it is allowed to nest lists. This allow us to model a matrix, for example:

In this lesson you will learn:
How to nest lists
and then access the elements accordingly. 
"""

list1 = [["New York", "Chicago", "Los Angeles"], ["Budapest", "Pecs", "Sopron"]]
print(list1[0][1]) # calling the item at position 1 for the nested list at position 0

students = {
	"Informatics" : ["Max", "Monika"],
	"History" : ["Erik", "Paula"]
}

print(students["Informatics"]) # can call the nested list item values
print(students["History"])