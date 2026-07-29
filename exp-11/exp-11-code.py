import cv2
import numpy as np

image = cv2.imread("image.jpg")

rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(pts1, pts2)

affine_image = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imwrite("affine_image.jpg", affine_image)

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", affine_image)

cv2.waitKey(0)
cv2.destroyAllWindows()