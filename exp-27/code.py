import cv2

img = cv2.imread("dragon.jpg")

cropped = img[180:500, 300:500]

img[700:1020, 300:500] = cropped

cv2.imwrite("crop_copy_paste_output.jpg", img)

cv2.imshow("Cropped Face", cropped)
cv2.imshow("Output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()