import cv2

img = cv2.imread("images.jpg", 0)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel_xy = cv2.magnitude(sobel_x, sobel_y)
sobel_xy = cv2.convertScaleAbs(sobel_xy)

cv2.imwrite("sobel_xy_output.jpg", sobel_xy)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY Edge", sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()