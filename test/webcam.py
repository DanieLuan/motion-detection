import cv2
import numpy as np

def display_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it if you have multiple cameras)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    black_mask = np.zeros((480, 640), dtype=np.uint8)
    triangle_vertices = np.array([[0, 0], [0, 480], [415, 480], [640, 160], [640, 0]], np.int32)
    cv2.fillPoly(black_mask, [triangle_vertices], 255)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        frame_roi = cv2.bitwise_and(frame, frame, mask=black_mask)

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame_roi)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_webcam()