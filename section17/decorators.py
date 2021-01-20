#def inner():
#	return "Hello World"

def outer(func):
	counter = 0
	def inner():
		nonlocal counter
		#return "Hello World"
		#print("inner() was called")
		print("Was called + " + str(counter) + " times")
		counter = counter + 1
		func()

	return inner

"""x = outer()
print(x)
print(x())"""

@outer
def do_something():
	print("do_something() was called")

#do_something = outer(do_something)

do_something()
do_something()
do_something()
do_something()
do_something()
do_something()

print("Decorator are very useful for design, but you don't need to use them all the time.")