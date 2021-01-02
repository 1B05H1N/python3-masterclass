"""
Dictionaries in Python

In this lesson I will introduce you to dictionaries. Why do you need these? 

You can save value assignments (e.g. phone book: A last name has a phone number).
You can change / remove / add elements later. 
Dictionaries you really need again and again.
We will also look at a few examples later in this course!
"""

d = {"Berlin":"BER", "Helsinki":"HEL", "Saigon":"SGN"} # key value pairs separated by a comma. They need to have immutable data types 
print(d)

print(d["Helsinki"])

d["Budapest"] = "BUD"
print(d)

# remove element
del d["Budapest"]
print(d)

# Query: Is there an element in the Dictionary?
if "Budapest" in d:
	print("Budapest is included in the dictionary") # doesn't show up since it's not in the dictionary 
if "Saigon" in d:
	print("Saigon is included in the dictionary") # shows up since it's in the dictionary 

# Access elements...
print(d["Saigon"])
print(d.get("Saigon"))
#print(d["Hong Kong"])

print(d.get("Hong Kong")) # cleaner than using print(d["value"])

rappers = {"MF DOOM":"Best", "Travis Scott":"Meh", "Kendrick Lamar":"GOAT"}
print(rappers)

rappers["ODB"] = "INSANE"
print(rappers)

if "Travis Scott" in rappers:
	print("Travis Scott makes OK music imo")

if "ODB" in rappers:
	print("RIP BIG BABY JESUS")

del rappers["Travis Scott"]
print(rappers)

#print(rappers["Travis Scott"])
print(rappers.get("Travis Scott"))
print(rappers.get("Meh"))

