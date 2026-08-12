import cv2

img = cv2.imread("vd.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

wide_gap = cv2.Canny(blur, 30, 200)
narrow_gap = cv2.Canny(blur, 150, 200)
optimal = cv2.Canny(blur, 50, 150)

cv2.imwrite("original.jpg", img)
cv2.imwrite("canny_wide_gap.jpg", wide_gap)
cv2.imwrite("canny_narrow_gap.jpg", narrow_gap)
cv2.imwrite("canny_optimal.jpg", optimal)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Wide Gap", cv2.WINDOW_NORMAL)
cv2.namedWindow("Narrow Gap", cv2.WINDOW_NORMAL)
cv2.namedWindow("Optimal", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original Image", 600, 400)
cv2.resizeWindow("Wide Gap", 600, 400)
cv2.resizeWindow("Narrow Gap", 600, 400)
cv2.resizeWindow("Optimal", 600, 400)

cv2.imshow("Original Image", img)
cv2.imshow("Wide Gap", wide_gap)
cv2.imshow("Narrow Gap", narrow_gap)
cv2.imshow("Optimal", optimal)

cv2.waitKey(0)
cv2.destroyAllWindows()