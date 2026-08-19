import cv2
import numpy as np

img = cv2.imread("ntr.jpg")

if img is None:
    print("Error: input.jpg not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(gx, gy)
gradient = cv2.convertScaleAbs(gradient)

output = cv2.addWeighted(gray, 1.0, gradient, 0.5, 0)

cv2.imwrite("output_gradient_masking.jpg", output)

cv2.imshow("Input Image", gray)
cv2.imshow("Output - Gradient Masking", output)

cv2.waitKey(0)
cv2.destroyAllWindows()