import os 

print(os.path.dirname(__file__))
folder = os.path.join(os.path.dirname(__file__), "..")
print(os.listdir("."))

print(folder)
print(os.listdir(folder))

folder = os.path.join(os.path.dirname(__file__), "folder")
print(os.listdir("."))

print(folder)
print(os.listdir(folder))

for file in os.listdir(folder):
	file_path = os.path.join(folder, file)
	if os.path.isdir(file_path):
		print(file+" is a folder")
	else:
		print(file+" is a file")

print(os.path.dirname(__file__))
filename = os.path.join(os.path.dirname(__file__), "folder", "subfolder", "file.txt")
print(filename)

with open(filename, "r") as file:
	for line in file:
		print(line)