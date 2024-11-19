import cv2
img=cv2.imread("Gohan.jpg",1)
B, G, R = cv2.split(img)
cv2.imshow("Gohan",img)
cv2.imshow("Blue Saturation Image", B)
cv2.imshow("Green Saturation Image", G)
cv2.imshow("Red Saturation Image", R)

cv2.waitKey(0)
cv2.destroyAllWindows()