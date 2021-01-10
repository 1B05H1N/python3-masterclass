"""
Exceptions in Python

In this lesson you will learn how to:

Catch multiple exceptions
Create your own exceptions
"""

try:
	print(5/0)
	with open("file.xyz", "r") as file:
		print(file)

except FileNotFoundError:
	print("File not found")
except ZeroDivisionError:
	print("You can't divide by zero")

def do_something():
	print(5/0)

try:
	do_something
except ZeroDivisionError:
	print("You can't divide by zero")

class InvalidEmailError(Exception):
	pass


def send_email(email_address, subject, content):
	if not "@" in email_address:
		raise InvalidEmailError("Email does not contain @ sign")

try:
	send_email("hello", "subject", "content")
except InvalidEmailError:
	print("Please enter a valid email address")