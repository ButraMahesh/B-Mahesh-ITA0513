import cv2

img = cv2.imread("dragon.jpg")

watermark = "MAHESH"

cv2.putText(img, watermark, (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 2)

cv2.imwrite("watermarked_output.jpg", img)

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()