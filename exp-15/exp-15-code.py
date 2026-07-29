import cv2
import numpy as np

image = cv2.imread("image.jpg")

pts1 = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])
pts2 = np.float32([[10, 100], [250, 50], [100, 250], [300, 300]])

A = []

for i in range(4):
    x, y = pts1[i]
    u, v = pts2[i]
    A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
    A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])

A = np.array(A)

_, _, V = np.linalg.svd(A)

H = V[-1].reshape(3, 3)

rows, cols = image.shape[:2]

dlt_image = cv2.warpPerspective(image, H, (cols, rows))

cv2.imwrite("dlt_transformation.jpg", dlt_image)

cv2.imshow("Original Image", image)
cv2.imshow("DLT Transformation", dlt_image)

cv2.waitKey(0)
cv2.destroyAllWindows()