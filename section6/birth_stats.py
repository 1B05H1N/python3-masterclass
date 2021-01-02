xs = []
ys = []

name = "Jose "
gender = "M"
state = "CA"

with open("../content/data/names.csv", "r") as file:
	counter = 0
	for line in file:
		counter = counter + 1
		line_split = line.strip().split(",")
		if line_split[1] == name and line_split[3] == gender and line_split[4] == state:
			# print(line_split)
			xs.append(int(line_split[2]))
			ys.append(int(line_split[5]))
			#break

"""print(xs)
print(ys)"""

%matplotlib inline
import matplotlib.pyplot as pyplot

plt.plot(xs, ys)
plt.show()