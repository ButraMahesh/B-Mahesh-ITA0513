import cv2
import numpy as np

img = cv2.imread("dragon.jpg")

if img is None:
    print("Image not found")
    exit()

img = cv2.resize(img, (640, 480))

gaussian_noise = np.random.normal(0, 25, img.shape).astype(np.float32)
gaussian_noisy = np.clip(img.astype(np.float32) + gaussian_noise, 0, 255).astype(np.uint8)

salt_pepper_noisy = img.copy()

amount = 0.05
num_pixels = int(amount * img.shape[0] * img.shape[1])

for _ in range(num_pixels):
    y = np.random.randint(0, img.shape[0])
    x = np.random.randint(0, img.shape[1])
    salt_pepper_noisy[y, x] = [255, 255, 255]

for _ in range(num_pixels):
    y = np.random.randint(0, img.shape[0])
    x = np.random.randint(0, img.shape[1])
    salt_pepper_noisy[y, x] = [0, 0, 0]

gaussian_filtered = cv2.GaussianBlur(gaussian_noisy, (9, 9), 0)

median_filtered = cv2.medianBlur(salt_pepper_noisy, 9)

cv2.imwrite("original.jpg", img)
cv2.imwrite("gaussian_noise.jpg", gaussian_noisy)
cv2.imwrite("gaussian_filtered.jpg", gaussian_filtered)
cv2.imwrite("salt_pepper_noise.jpg", salt_pepper_noisy)
cv2.imwrite("median_filtered.jpg", median_filtered)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Noise", gaussian_noisy)
cv2.imshow("9x9 Gaussian Filter", gaussian_filtered)
cv2.imshow("Salt and Pepper Noise", salt_pepper_noisy)
cv2.imshow("9x9 Median Filter", median_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()