import cv2

image = cv2.imread("image.jpg")

clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("clockwise_image.jpg", clockwise)
cv2.imwrite("counter_clockwise_image.jpg", counter_clockwise)

cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()