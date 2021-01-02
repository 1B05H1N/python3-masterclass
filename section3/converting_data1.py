# string -> integer (whole number)
a = "5"
b = "6" 
print(a + b) # it's just concatenating the strings
print(int(a) + int(b)) # converts string to integer 

# string -> floating point number, integers only understand whole numbers
a = "5.5"
b = "6.5"

# we use the float data type
print(float(a) + float(b))

# integer + string
age = 30
print("I am " + str(age) + " years old")