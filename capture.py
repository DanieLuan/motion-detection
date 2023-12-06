import cv2
import time
from datetime import datetime

def print_and_save_image():
    camera_index = 0

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Could not open USB camera.")
        return

    ret, frame = cap.read()
    
    current_time = datetime.now().strftime("%m-%d-%Y-%H:%M:%S")
    cv2.imwrite(f'imgs/{current_time}.jpg', frame)
    print("Image saved as img.jpg")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        print_and_save_image()
        time.sleep(60)  # Sleep for 60 seconds (1 minute)