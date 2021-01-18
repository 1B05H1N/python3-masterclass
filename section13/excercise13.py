"""
task 1

Complete the shortest_word() function: pass several strings to it (NO list strings!), of which it returns the string with the fewest characters. 

Note: Use variable parameters (with asterisks * or a double asterisks **)!
"""
def shortest_word(first, *words):
	shortest = first
	for word in words:
		if len(word) < len(shortest):
			shortest = word
		return shortest

print(shortest_word("Max", "Paula", "Monica", "Tim", "Jo"))

"""
task 2 

a.) 
Sort the tuples in the list tuples in ascending order of their sum!

Note: Write a normal function first and then solve the task again with a lambda function. 
"""

tuples = [(10,2), (4,1), (0,17), (3,3), (5,7), (11,3)]

def tuples_sort(a):
	return a[0] + a[1]

tuples.sort(key=tuples_sort)
print(tuples)

tuples = [(10,2), (4,1), (0,17), (3,3), (5,7), (11,3)]

tuples.sort(key=lambda t: t[1])
print(tuples)

"""
b.)
Sort the list names by last name. You can assume that all names in the list contain only one first name. The format of the names is always "first name surname".

First think about how to get the last name and then write the function you pass to the .sort() function. 

Note: Write a normal function first and then solve the task using a lambda function.
"""

names = ["Elif Else", "Steven Moser", "Anna Boa", "Anton Adel", "Conny Coder", "Tine Turner", "Willy Cordes"]

def tuples_sort(s):
	return s.split()[1]

names.sort(key=tuples_sort)
print(names)

names = ["Elif Else", "Steven Moser", "Anna Boa", "Anton Adel", "Conny Coder", "Tine Turner", "Willy Cordes"]

names.sort(key=lambda s: s.split()[1])
print(names)

"""
c.)

Sort the list sentences in descending order by the number of words contained in each element of sentences. You can assume that all the words in the sentences are properly separated by spaces. :-)

Think about how to determine the number of words in a sentence first. 

Note: Write a normal function first and then solve the task again with a lambda function. 
"""

sentences = ["They kept walking along the beach.", "The dog barked loduly.", "He slipped.", "She laughed loud."]

def tuples_sort(a):
	return len(a.split())
sentences.sort(key=tuples_sort, reverse=True)
print(sentences)

sentences = ["They kept walking along the beach.", "The dog barked loduly.", "He slipped.", "She laughed loud."]

sentences.sort(key=lambda a: len(a.split()), reverse=True)
print(sentences)

"""
Extra task (difficult)

Change the following code so that the list 1 is no longer overwritten within the make_row() function. The list that make_row() outputs should therefore be identical to the previous list. However, 1 is to be output in its original form at the end.
"""

l = ["o", "x", "o"]

def make_row(row):

	new_row = row[:]
#	new_row = [i for i in row]
#	new_row = row.copy()
	new_row[2] = "x"
	print(row)

make_row(l)
print(l)