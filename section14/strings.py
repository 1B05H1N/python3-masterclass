#Working with strings

w = "Hello"
print(w.upper())
print(w)

w_upper = w.upper()
print(w_upper)

w_lower = w.lower()
print(w_lower)

print("HEllo".lower())
print("hello".upper())

sentence = "Is the weather good today???"

if sentence.endswith("???"):
	print("The sentence ends with three question marks")

if sentence.startswith("Is"):
	print("The sentence starts with 'Is'")

"		Hello World.		".strip()

word = "___Hello.___"
print(word.strip("_."))
print(word.lstrip("._"))
print(word.rstrip("_."))

sentence1 = "Is the weather good today, and tomorrow too???"
print(sentence1.rstrip("!?.,"))

sentence2 = "Is the weather good today, and tomorrow too???"
print(sentence2.find("eat"))
print(sentence2.find("!"))

print(sentence2.replace(",", ";"))
print(sentence2.replace("oo", "00"))
print(sentence2.replace("w", "\/\/"))
print(sentence2.replace("and","or"))

