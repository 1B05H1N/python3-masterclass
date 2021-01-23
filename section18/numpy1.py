import matplotlib.pyplot as plt

xs = []
for x in range(0, 10):
	xs.append(x)

ys = []
for x in xs: 
	ys.append(x**2)

plt.plot(xs, ys)
#plt.show()

#import numpy 
import numpy as np

# create array of integers 0-9 and store as xs variable
xs = np.arange(10)

ys - xs ** 2

plt.plot(xs, ys)
#plt.show()

# create array with array() function

np.array([1,2,3,4,5,10])

np.arange(1,11)

np.arange(10)

np.zeros(10)

np.ones(10)

np.arange(10) + 3

np.arange(10) * 3

a = np.array([1,2,3,4,5,10])
print(a.mean())
print(a.min())
print(a.max())
print(a.std())