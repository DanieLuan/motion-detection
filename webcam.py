import cv2

def display_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it if you have multiple cameras)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
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
    
def detect_connected_cameras():
    index = 0

    while True:
        cap = cv2.VideoCapture(index)
        ret, frame = cap.read()
        
        if not ret:
            cap.release()
            cv2.destroyAllWindows()
        else:
            print(f"Camera {index} is connected!!!!!!!!!!!!!")

        index += 1
        if index > 30:
            break
        
        
def print_and_save_image():
    camera_index = 0

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Could not open USB camera.")
        return

    ret, frame = cap.read()


    cv2.imwrite('captured_image.jpg', frame)
    print("Image saved as captured_image.jpg")


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print_and_save_image()