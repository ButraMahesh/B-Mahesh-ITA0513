import cv2
import os

folder = r"C:\Users\User\OneDrive\Documents\ITA05\exp-8"

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
    exit()

bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imwrite(os.path.join(folder, "bigger_image.jpg"), bigger)
cv2.imwrite(os.path.join(folder, "smaller_image.jpg"), smaller)

print("Images saved successfully")

cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()