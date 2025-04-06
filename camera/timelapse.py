# timelapse.py
# Takes periodic images for time-lapse compilation

import cv2
import time
import os

def create_timelapse(duration=60, interval=5, output_dir="timelapse"):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Camera not accessible")

    frames = duration // interval
    for i in range(frames):
        ret, frame = cap.read()
        if ret:
            filename = f"{output_dir}/frame_{i:03}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Captured {filename}")
        time.sleep(interval)

    cap.release()

if __name__ == "__main__":
    create_timelapse(duration=60, interval=10)
