import cv2

img=cv2.imread("Gohan.jpg",0)
cv2.imshow("Gohan",img)

cv2.waitKey(0)
cv2.destroyAllWindows()