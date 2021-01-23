#Numpy:Filter arrays

import numpy as np

a = np.array([1,2,3,4])
print(a)

b = np.array([False, True, True, False])
print(b)

aa = a[b] #filter values out of array a using logic from array b
print(aa)

c = a >= 3
print(c)

d = a[c]
print(d)

print(a[a >= 3])

