import cv2
import numpy as np

img = cv2.imread("India gate.jpg")

if img is None:
    print("Image not found")
    exit()

height, width, channels = img.shape
rgb_payload = width * height * 3
gray_payload = width * height

rgb_per_second = rgb_payload * 30
gray_per_second = gray_payload * 30
print("Image Resolution:", width, "x", height)
print("Number of Channels:", channels)
print("\nRGB Data:")
print("Data per Frame:", rgb_payload, "bytes")
print("Data per Second:", rgb_per_second, "bytes")
print("Payload:", rgb_per_second / 1000000, "MB/s")
print("\nGrayscale Data:")
print("Data per Frame:", gray_payload, "bytes")
print("Data per Second:", gray_per_second, "bytes")
print("Payload:", gray_per_second / 1000000, "MB/s")
reduction = ((rgb_per_second - gray_per_second) / rgb_per_second) * 100
print("Data Reduction:", reduction, "%")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold_value = 200
_, threshold_image = cv2.threshold(
    gray, threshold_value, 255, cv2.THRESH_BINARY
)
coordinates = np.column_stack(np.where(threshold_image > 0))
print("\nMid-Level Processing:")
print("Threshold Value:", threshold_value)
print("Pixels Above Threshold:", len(coordinates))
cv2.imwrite("grayscale.jpg", gray)
cv2.imwrite("threshold.jpg", threshold_image)
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Threshold Image", threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()