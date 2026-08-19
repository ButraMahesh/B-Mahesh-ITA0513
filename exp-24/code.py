import cv2

img = cv2.imread("NTR.jpg")

if img is None:
    print("Error: input.jpg not found")
    exit()

blur = cv2.GaussianBlur(img, (5, 5), 0)

output = cv2.addWeighted(img, 2.5, blur, -1.5, 0)

cv2.imwrite("output_high_boost.jpg", output)

cv2.imshow("Input Image", img)
cv2.imshow("Output - High Boost Mask", output)

cv2.waitKey(0)
cv2.destroyAllWindows()