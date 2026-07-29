import cv2
import numpy as np

image = cv2.imread("image.jpg")

rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])
pts2 = np.float32([[10, 100], [250, 50], [50, 250], [300, 300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imwrite("perspective_image.jpg", perspective_image)

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", perspective_image)

cv2.waitKey(0)
cv2.destroyAllWindows()