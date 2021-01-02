print("Hello World") # contents between " " are called strings

name = "Max"
print("Hi, I'm " + name) # we concatenate the string with the name variable 

age = "22" # storing age as a string as opposed to a int. We will get an error if we tried to call the int this was
print("I am " + age + " years old")

age = 22
print("I am " + str(age) + " years old") # use string method to print int