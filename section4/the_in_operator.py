# membership operator, operator tests for membership in a sequence (list, or tuple)

students = ["max", "monika", "erik", "franziska"]
print("monika" in students)
print("moe" in students)

if "monika" in students:
	print("yes, monika studies here")
else:
	print("no, monika doesn't study here")
if "moe" in students:
	print("yes, moe studies here")
else:
	print("no, moe doesn't study here")

# by the way: this also works for strings

sentence = "yes, monika studies here!"

if "no" in sentence:
	print("yes")
else:
	print("no")