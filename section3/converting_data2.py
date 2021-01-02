# list -> string
students = ["Max", "Monika", "Erik", "Franziska"]
students_string = "Max, Monika, Erik, Franziska"
print(", ".join(students)) # join function that will join list elements together

students_as_string = ", ".join(students)
print("At our university, student those people: " + students_as_string)

# strings -> list

i = "Max, Monika, Erik, Franziska"
print(i.split(", ")) # split function will create a list out of a string using a delimiter following split("<delimiter>")

a = "I am a sentence with many words"
print(len(a.split(" "))) # split will create a list out of string, len will give us length of list, and print will print to console