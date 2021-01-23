#Matplotlib diagram types

import matplotlib.pyplot as plt 

plt.pie([1,2,3])
plt.show()

plt.bar([1,2,3], [5,6,5])
plt.show()

plt.scatter([1,2,3],[0,3,6,5], color="red", marker="x")
plt.show()