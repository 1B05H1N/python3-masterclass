file = open("read.txt", "r")
for line in file:
	print(line)

print("Hel\nlo") # \n escapes the next character
print("World")

file = open("read.txt", "r")
for line in file:
	print(line[-1])

file = open("read.txt", "r")
for line in file:
	print(line.strip()) # strip gets rid of the line break and makes everything look clean