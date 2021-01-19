import os

folder = os.path.join(os.path.dirname(__file__), "names")

counter = 0

files = os.listdir(folder)
print(files)
for filename in files:
	f = os.path.join(os.path.dirname(__file__), "names", filename)
	with open(f, "r", encoding="utf=8") as file:
		for line in file:
			#print(line.strip().split(" "))
			l = line.strip().split(" ")
			firstname = l[0]
			if firstname == "Max":
				counter += 1
			"""if len(l) != 2:
													print(l)
													print(f)"""

		"""if firstname == "Max":
						counter += 1"""

print(counter)

#11 Max's