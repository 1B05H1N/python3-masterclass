# the not - operator

age = 25

if not age >= 30:
	print("executed")

if age < 30:
	print("executed")

names = ["max", "nadine"]

if "moe" not in names:
	print("moe is not in the list")
if not "moe" in names:
	print("moe is not in the list")

# same thing but if <thing> not is easier to read than if not <thing>

if "moe" in names:
	print("moe is there")
else:
	print("moe is not in the list")
