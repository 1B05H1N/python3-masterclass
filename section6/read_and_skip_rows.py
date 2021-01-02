with open("file.csv") as file:
	for line in file:
		data = line.strip().split(";")
		if data[2] == "BER" or data[2] == "BUD": 
			print(data[2])
			print(data)

with open("file.csv") as file:
	for line in file:
		data = line.strip().split(";")
		if int(data[1]) >= 2000000:
			print(data)

with open("file.csv") as file:
	for line in file:
		data = line.strip().split(";")
		if int(data[1]) >= 2000000:
			continue
			
		print(data)

with open("file.csv") as file:
	for line in file:
		data = line.strip().split(";")
		if int(data[1]) >= 2000000:
			continue

		if data[2] == "BUD":
			continue

		print(data)