#The DefaultDict module

from collections import defaultdict

def generate():
	print("generate() was called")
	return 0 

d = defaultdict(generate)
d["does_not_exist"] = d["does_not_exist"] + 5
print(d["does_not_exist"])

print(int())
p = defaultdict(int)

words = ["Hello", "Hello", "Hello", "World", "World"]
for word in words:
	p[word] = p[word]+1

print(p)