import cv2

def display_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it if you have multiple cameras)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_webcam()