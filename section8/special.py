"""
In Python there are a few special methods that our class can implement...
With that, you can make sure that: 

Your class get's a printable string reprsentation directly,
You can calculate the len(variable).
"""

class PhoneBook():

	def __init__(self):
		self.__entries = {}

	def add(self, name, phone_number):
		self.__entries[name] = phone_number

	def get(self, name):
		if name in self.__entries:
			return self.__entries[name]
		else:
			return None

	def __str__(self): # creates string out of an object (similar to 2 string method in d#)
		return "PhoneBook(" + str(self.__entries) + ")"

	def __repr__(self): # deifine what it should do
		return self.__str__()

	def __len__(self):
		return len(self.__entries)

book = PhoneBook()
book.add("Miller", "+123456987")
book.add("Doe", "+176543567")
book.add("Smith", "+12443567")
book.add("Brewer", "+1743143567")

print(len(book))
print(book)