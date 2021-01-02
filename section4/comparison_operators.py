if  5 < 6:
	print("yes")
else:
	print("no")

print(6<5) # defaults to false/true boolean
print(5<6)

b = False # important that you use a capital F in false so Python knows it's a boolean
print(b)

result = 5 < 6
if result:
	print("5 is less than 6")

print(result) # result variable is now a boolean (can only be true or false)

"""
there are equal comparisons
"""

print(5 == 5) # double '=' is always a comparison
print(5 == 4)

word = "hello"
print(word == "hello")
print(word == "word") # we're comparing contents

word = "hello"
print(word != "hello") # != means not equal
print(word != "word")

print(5 < 5)
print(5 <= 5) # less than or equal to 

print(5 > 5)
print(5 >= 5) # greater than or equal to

if True or False:
	print("yes")