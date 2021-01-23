import matplotlib.pyplot as plt 
import numpy as np 
import cv2

img = cv2.imread("ms.jpg")

print(img[0][0])

r = np.array([1,2,3,100], dtype="uint8")
# 0 -255
r = r +250
#print(r)

increased = img + 100

print(increased[0][0])

z = np.zeros([1000, 1500, 3], dtype="uint8") + 50
#print(z)

increased = cv2.add(img,z)
print(img[0][0])
print(z[0][0])
print(increased[0][0])

i = cv2.cvtColor(increased, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()

