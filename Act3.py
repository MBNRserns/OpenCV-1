import cv2
import os

img=cv2.imread("Gohan.jpg",0)
cv2.imshow("Gohan",img)
path="C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-1"
os.chdir(path)
cv2.imwrite("black-n-white-gohan.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()