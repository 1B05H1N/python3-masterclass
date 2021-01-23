import numpy as np 

a = np.array([1,2,3,4,5,6,7,8])

reshaped = a.reshape((2,4))
print(reshaped[0])
print(reshaped[1])
print(reshaped)

reshaped1 = a.reshape((-1,4))
print(reshaped1)

reshaped2 = a.reshape((4,-1))
print(reshaped2)

b = np.array([[1,2,3], [4,5,6]])
print(b)
reshapedb = b.reshape(-1)
print(reshapedb)

c = np.array([1,2,3,4,5,6,7,8])
c = c.reshape(4,2)
print(c)