
"""
Encapsulating data

In this lesson you will learn an example of why it can be worth encapsulating data with object orientation.

Advantage: Clear layout, prerequisite for building larger applications (modular)
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

book = PhoneBook()
book.add("Miller", "123456987")
book.add("Fisher", "876543567")

print(book.get("Miller"))