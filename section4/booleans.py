age = 35

if age >= 30 and age <= 39:
	print("this person is in their 30's")
else:
	print("this person is not in their 30's")

age = 45
if age < 30 or age >=40:
	print("this person is not in their 30's")
print(age < 30)
print(age >= 40)

age = 25
above_30 = age >= 30 
print(above_30)

age = 25
above_20 = age >= 20
print(above_20)

if age >= 20:
	print("if statement was executed")

if True:
	print("hi there")

print(True and True)
print(True and False)
print(False and False)
print(False and True)

print(True or True)
print(True or False)
print(False or False)
print(False or True)

country ="gb"
age = 20
if(country == "us" and age >= 21) or (country != "us" and age >= 18):
	print("This person may drink alcohol")
else:
	print("this person may not drink alcohol")