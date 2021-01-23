import matplotlib.pyplot as plt 
import numpy as np 
import cv2

img = cv2.imread("ms.jpg")

cv2.rectangle(img, (400,200), (500,500), (0,0,255), 10)

i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()
