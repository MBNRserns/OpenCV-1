import cv2

#cv2.IMREAD_COLOR (1) => Specify to load the image in color. excludes transaperency
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

img=cv2.imread("Gohan.jpg",1)
cv2.imshow("Gohan SSJ2",img)

cv2.waitKey(0)
cv2.destroyAllWindows()