#OpenCV: Edit images with Python

import matplotlib.pyplot as plt 
import numpy as np 
import cv2

img = cv2.imread("ms.jpg")
#print(img)

img.shape
a = np.array([[1,2,3],[4,5,6]])

print(a.shape)

#cv2.imshow("img", img)


print(img[0][0])

i = cv2.(img, cv2.COLOR_BGR2RGB)

plt.imshow(i)
plt.show()

g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(g.shape)
print(g[0][0])
plt.imshow(g, "gray")
plt.show()

