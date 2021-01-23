import matplotlib.pyplot as plt 
import numpy as np 
import cv2

img = cv2.imread("ms.jpg")

#cv2.rectangle(img, (400,200), (500,500), (0,0,255), 10)

i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(i)
#plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, "gray")
#plt.show()

classifier  = cv2.CascadeClassifier("C:/Users/account/Documents/github/Learning/content/data/haarcascades/haarcascade_frontalface_alt2.xml")

faces = classifier.detectMultiScale(gray,minNeighbors = 1)
print(faces)

c = img.copy()
for face in faces:
	x, y, w, h = face
	cv2.rectangle(c, (x,y),(x+w,y+h),(0,255,0),10)
	print(face)

i = cv2.cvtColor(c, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()