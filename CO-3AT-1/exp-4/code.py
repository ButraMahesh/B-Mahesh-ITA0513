import cv2
import numpy as np

img = cv2.imread("tom.jpg")

if img is None:
    print("Image not found")
    exit()

img = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

ks = [0.01, 0.08, 0.15]

outputs = []

for k in ks:
    dst = cv2.cornerHarris(gray, 2, 3, k)
    dst = cv2.dilate(dst, None)

    result = img.copy()

    threshold = 0.01 * dst.max()
    result[dst > threshold] = [0, 0, 255]

    outputs.append((k, result))

cv2.imwrite("original.jpg", img)
cv2.imwrite("harris_k_001.jpg", outputs[0][1])
cv2.imwrite("harris_k_008.jpg", outputs[1][1])
cv2.imwrite("harris_k_015.jpg", outputs[2][1])

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Harris k=0.01", cv2.WINDOW_NORMAL)
cv2.namedWindow("Harris k=0.08", cv2.WINDOW_NORMAL)
cv2.namedWindow("Harris k=0.15", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original", 600, 400)
cv2.resizeWindow("Harris k=0.01", 600, 400)
cv2.resizeWindow("Harris k=0.08", 600, 400)
cv2.resizeWindow("Harris k=0.15", 600, 400)

cv2.imshow("Original", img)
cv2.imshow("Harris k=0.01", outputs[0][1])
cv2.imshow("Harris k=0.08", outputs[1][1])
cv2.imshow("Harris k=0.15", outputs[2][1])

cv2.waitKey(0)
cv2.destroyAllWindows()