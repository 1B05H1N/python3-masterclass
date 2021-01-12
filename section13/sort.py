"""
Sort data

Often you have the problem that you want to sort a list, for example. Python already provides a ready-made function here, but we want to control it correclty. In this lesson you will learn how to sort data in Python, and influence the sorting.
"""

l = ["Max", "Monica", "Eric", "Paula"]
l.sort()
print(l)


l = ["Max", "Monica", "Eric", "Paula"]
l.sort(reverse=True)
print(l)

def get_length(item):
	return len(item)
l = ["Max", "Monica", "Eric", "Paula"]
l.sort(key=get_length)

l = ["Max", "Monica", "Eric", "Paula"]
l.sort(key=len)
print(l)

d = {"Cologne":"CDN", "Budapest":"BUD", "Saigon":"SGN"}

print(sorted(d, reverse=True))

l = ["Max", "Monica", "Eric", "Paula"]
l.sort()
print(l)

l = ["Max", "Monica", "Eric", "Paula"]
l2 = sorted(l)
print(l)
print(l2)