"""
Further data structure: PriorityQueue
In this lesson you will learn another data structure: PriorityQueue

This is a queue that sorts the entries for us automatically!
"""
import queue

q = queue.PriorityQueue()

q.put((10, "Hello World"))
q.put((15, "Mars"))
q.put((5, "IMPORTANT"))

q.get()
q.get()
q.get()


text = "A A A A A A A A A B B B B B B B C C C C C C D D D"
d={}
for word in text.split(" "):
	if word in d:
		d[word] = d[word] + 1
	else:
		d[word]=1

pq = queue.PriorityQueue()

for word, number in d.items():
	pq.put((-number, word))

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())


