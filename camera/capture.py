# capture.py
# Captures a single image from Raspberry Pi camera

import cv2

def capture_image(filename="plant_snapshot.jpg"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Camera not accessible")

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("Failed to capture image")
    cap.release()

if __name__ == "__main__":
    capture_image()
