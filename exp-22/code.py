import cv2
import numpy as np

img = cv2.imread("msd.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(gray, -1, kernel)

cv2.imwrite("sharpened_positive_output.jpg", sharpened)

cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()