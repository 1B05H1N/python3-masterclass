"""
Excursus: Drawing graphics
In this lesson you will learn how to draw nice graphics

Step 1: Embed + configure metplotlib inline
"""
%matplotlib inline
import matplotlib.pyplot as plt 

# Step 2: Draw graphic

xs = [1, 2, 5]
ys = [4, 7, 1]

plt.plot(xs, ys)
plt.show()