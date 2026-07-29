import cv2

image = cv2.imread("image.jpg")

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

eroded = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()