"""
Python knowledge: generators

This lesson is about another python concept that can simplify our crawler a bit: Generators

Problem: Sometimes you are only interested in the first 5 entries, sometimes you only want to read in all entires. How do you get the .fetch() method to automatically detect how many entries I am interested in? 

In this lesson you will learn:
	
	What generators are
	And how to use them in Python
"""

def gen_list():
	list1=[]
	for i in range(0,10):
		print("list: " + str(1))
		list1.append(i)
	print(list1)
	return list1

for element in gen_list():
	print("for: " + str(element))

# generator approach 

def gen_generator():
	for i in range(0,10):
		print("gen: " + str(i))
		yield i 

for element in gen_generator():
	print("for: " + str(element))

for element in gen_generator():
	if element == 4:
		break
	print("for "+ str(element))