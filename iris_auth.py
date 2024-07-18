import cv2
import numpy as np
import os
import getpass

# Predefined password
AUTHORIZED_PASSWORD = "open_sesame"
# Directory where example iris images are stored
STORED_IRIS_DATA_PATH = "stored_iris_data"

def capture_iris_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            return None

        cv2.imshow('Capture Iris Image', frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):  # Press 'c' to capture
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame

def process_iris_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    _, thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)
    return thresh

def load_example_iris_data(directory):
    example_data = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                example_data.append(image)
    return example_data

def recognize_iris(processed_image, stored_images):
    processed_image = cv2.resize(processed_image, (100, 100))  # Resize processed image for consistency (example size)
    
    for stored_image in stored_images:
        stored_image = cv2.resize(stored_image, (100, 100))  # Resize stored image for consistency (example size)
        
        difference = cv2.absdiff(processed_image, stored_image)
        result = np.sum(difference) / 255
        if result < 1000:  # Adjust threshold as needed
            print("Match found: Access Granted")
            return True
    return False


if __name__ == "__main__":
    # Prompt the user to enter the password
    password = getpass.getpass(prompt="Enter password: ")
    
    if password != AUTHORIZED_PASSWORD:
        print("Access Denied: Incorrect password")
        exit(1)

    # Load example iris data
    stored_iris_data = load_example_iris_data(STORED_IRIS_DATA_PATH)
    if not stored_iris_data:
        print("Error: No example iris data found.")
        exit(1)

    frame = capture_iris_image()
    if frame is not None:
        processed_image = process_iris_image(frame)
        if recognize_iris(processed_image, stored_iris_data):
            exit(0)
        else:
            print("Access Denied: Iris not recognized")
            exit(1)
    else:
        print("Access Denied: Could not capture iris image")
        exit(1)
