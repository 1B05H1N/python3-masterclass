"""
Further data structure: Queue

In this lesson you will learn another data structure: Queue

This is optimized for the following operations:

Add entry
Remove entry form the beginning
"""

import queue
q = queue.Queue()

q.put("Hello")
q.put("World")
q.put("Hello")
q.put("Mars")
q.put("Hello")
q.put("Pluto")

print(q.get())

print(q.get())

while not q.empty():
	element = q.get()
	print(element)