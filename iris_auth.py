import cv2
import numpy as np

def authenticate_iris():
    def recognize_iris(image):
        # Dummy logic: recognize iris if the mean pixel value is above a threshold
        return np.mean(image) > 50

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return False

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return False

    cap.release()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if recognize_iris(gray):
        print("Iris recognized successfully.")
        return True
    else:
        print("Iris recognition failed.")
        return False

if __name__ == "__main__":
    if authenticate_iris():
        exit(0)
    else:
        exit(1)
