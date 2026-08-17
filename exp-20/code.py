import cv2
import numpy as np

img = cv2.imread("dragon.jpg")

kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

laplacian = cv2.filter2D(img, cv2.CV_64F, kernel)
sharpened = cv2.convertScaleAbs(img.astype(np.float64) - laplacian)

cv2.imwrite("sharpened_output.jpg", sharpened)

cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()