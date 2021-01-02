with open("file.csv") as file:
	for line in file:
		# print(line)
		# print(line.strip().split(";"))
		data = line.strip().split(";")
		print(data)
		print(data[0] + " has " + data[1] + " inhabitants. Airport " + data[2])