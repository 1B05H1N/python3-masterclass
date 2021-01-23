
import matplotlib.pyplot as plt

xs = []
for x in range(0, 10):
	xs.append(x)

ys = []
for x in xs: 
	ys.append(x**2)

plt.plot(xs, ys)
plt.show()