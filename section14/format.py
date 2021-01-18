#format strings

n = 5
print("I have " + str(n) + " dogs.")
print("Yo tengo " + str(n) + " perros.")

translations = {
	"number_of_dogs":"I have XXX dogs"
}
print(translations["number_of_dogs"].replace("XXX", str(n)))

translations = {
	"number_of_dogs":"I have {0} dogs"
}
print(translations["number_of_dogs"].format(n))

print("I have {0} dogs".format(n))

print("I have {0} {1} and {0} dogs".format(n, "Cats"))

print("Pi has the value of : {0:.3f}".format(3.14159))

print("I have {number:.3f} {animals}".format(number=5, animals="Cats"))