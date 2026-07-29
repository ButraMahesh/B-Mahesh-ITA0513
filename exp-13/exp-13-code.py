import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("perspective_video.mp4", fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    pts1 = np.float32([[100, 100], [500, 100], [100, 400], [500, 400]])
    pts2 = np.float32([[50, 150], [550, 50], [50, 350], [550, 450]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    transformed = cv2.warpPerspective(frame, matrix, (640, 480))

    out.write(transformed)

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformation Video", transformed)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()