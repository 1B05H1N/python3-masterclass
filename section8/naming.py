"""
Styleguide - Naming classes and variables

Basically it doesn't matter how we name a class / variable in Python. Our program will work either way. 

But: For Python there are some style guides on how we can write "nice code". In this lesson I would like to go through the most important points of...

https://www.python.org/dev/peps/pep-0008/

How can (should) we name variables / classes / functions, especially if the names should consist of several words? 

In Python, this is done by convention:
	PascalCase(SeveralWords)
	sneak_case(several_words)

Unlike other programming languages, this is not used: 
	camelCase(severalWords)
"""

# Class names in PascalCase
# But this example is too long ;-)
class ThisIsTooLongSeriouslyTooooLong():
	def __init__(self):
		print("TEST")

		#Function name in sneak_case

		def i_am_a_function(self):
			print("asdf")

# Variable names also in sneak_case; but at most three words ;-)
several_words = ThisIsTooLongSeriouslyTooooLong

print(several_words)

# create descriptive class names with pascal case that are long but not too long 
# create short variable names with sneak case