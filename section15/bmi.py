print("BMI Calculator")

weight_str = input("Please enter your weight in kg: ")
height_str = input("Please enter your height in m: ")

print(weight_str)
print(height_str)

weight = float(weight_str.replace(",","."))
height = float(height_str.replace(",","."))

bmi = weight/height**2

print("Your BMI is: " + str(rount(bmi,1)))