import os

print(__file__)
print(os.path.dirname(__file__))

with open(os.path.join(os.path.dirname(__file__), "/argv.py"), "r") as file:
	for line in file:
		print(line)

#print(os.listdir("."))