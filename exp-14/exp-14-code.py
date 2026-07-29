import cv2
import numpy as np

image = cv2.imread("image.jpg")

rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])
pts2 = np.float32([[10, 100], [250, 50], [100, 250], [300, 300]])

H, status = cv2.findHomography(pts1, pts2)

homography_image = cv2.warpPerspective(image, H, (cols, rows))

cv2.imwrite("homography_image.jpg", homography_image)

cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformation", homography_image)

cv2.waitKey(0)
cv2.destroyAllWindows()