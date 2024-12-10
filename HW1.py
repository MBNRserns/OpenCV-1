import cv2
import os

img=cv2.imread("Piccolo.jpg")
cv2.imshow("Piccolo",img)

#Color
img1=cv2.imread("Piccolo.jpg",1)
img2=cv2.imread("Piccolo.jpg",0)
img3=cv2.imread("Piccolo.jpg",-1)
cv2.imshow("Color",img1)
cv2.imshow("Grayscale",img2)
cv2.imshow("Unchanged",img3)

#BGR
B, G, R = cv2.split(img)
cv2.imshow("Blue Saturation Image", B)
cv2.imshow("Green Saturation Image", G)
cv2.imshow("Red Saturation Image", R)

#Changing Image

path="C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-1"
os.chdir(path)
cv2.imwrite("Grayscale-Piccolo.jpg",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()