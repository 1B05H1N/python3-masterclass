import numpy as np 

a = np.array([1,2,3])
print(a*2)

class MyArray():
	def __int__(self, list1):
		self.list1 = list1

	def __mul__(self, other):
		nlist1 = []
		for element in self.list1:
			nlist1.append(element * other)
		return nlist1

a1 = MyArray([1,2,3])
b  = a1*2 
b = a1.__mul__(2)
print(a1.list1)
print(b)