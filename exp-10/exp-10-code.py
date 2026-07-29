import cv2
import numpy as np

image = cv2.imread("image.jpg")

rows, cols = image.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])

moved_image = cv2.warpAffine(image, M, (cols, rows))

cv2.imwrite("moved_image.jpg", moved_image)

cv2.imshow("Original Image", image)
cv2.imshow("Moved Image", moved_image)

cv2.waitKey(0)
cv2.destroyAllWindows()