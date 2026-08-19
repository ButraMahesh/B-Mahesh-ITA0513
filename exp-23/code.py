import cv2

img = cv2.imread("ntr.jpg")

if img is None:
    print("Error: input.jpg not found")
    exit()

blur = cv2.GaussianBlur(img, (9, 9), 10)

output = cv2.addWeighted(img, 2.0, blur, -1.0, 0)

cv2.imwrite("output_unsharp_masking.jpg", output)

cv2.imshow("Input Image", img)
cv2.imshow("Output - Unsharp Masking", output)

cv2.waitKey(0)
cv2.destroyAllWindows()