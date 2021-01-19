# how to pass a parameter to your program

#user_input = input("Please enter something")

#print(user_input)

import sys

#print(sys.argv)

'''
if len(sys.argv) >= 2:
	print("More than just the file")
'''

if len(sys.argv) >= 2:
	filename = sys.argv[1]
	file = open(filename,"r")

	counter = 0
	for line in file:
		counter += 1

	print(counter)

else:
	print("File path is missing!")

