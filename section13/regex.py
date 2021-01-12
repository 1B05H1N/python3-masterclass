"""
Basics: Regular Expression

Regular expressions allow you to search strings even more flexibility. For example, you can use a regular expression to find all numbers in a string or validate that an email address could exist in principle. 

But how do they work?
"""

# can search for patterns in a defined string

import re

sentence = "I have 30 dogs that need 4 litres of water and 2 kg of food each."
re.findall("[0-9]+", sentence)

sentence = "I have 30 dogs that need 4 litres of water and 2 kg of food each."
re.search("[0-9]+", sentence)

sentence = "I haveeeee 30 dogs that need 4 litres of water and 2 kg of food each."
re.search("have?", sentence)

print(re.search("the*", "Hello th hello"))
print(re.search("the*", "Hello the hello"))
print(re.search("the*", "Hello thee hello"))

print(re.search("the+", "Hello th hello"))
print(re.search("the+", "Hello the hello"))
print(re.search("the+", "Hello thee hello"))

print(re.search("[123456789]", "Hello 123 hello"))

print(re.findall("[123456789]+", "Hello 123 hello"))

print(re.findall("[123456789]+", "Hello 12345678 hello"))

print(re.findall("[123456789]+", "Hello 1234568g987 hello"))

print(re.findall("[a-z]+", "Hello 123 hello"))

#regexer.com