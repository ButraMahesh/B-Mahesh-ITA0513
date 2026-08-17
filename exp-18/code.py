import cv2

img = cv2.imread("images.jpg", 0)

sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imwrite("sobel_y_output.jpg", sobel_y)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y Edge", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()