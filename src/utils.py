import cv2
import time
import numpy as np
from loguru import logger

def camera_mask():
    black_mask = np.zeros((480, 640), dtype=np.uint8)
    triangle_vertices = np.array([[0, 0], [0, 480], [415, 480], [640, 160], [640, 0]], np.int32)
    cv2.fillPoly(black_mask, [triangle_vertices], 255)
    return black_mask

def is_movement_detected(cap, start_time):
    prvs = None
    elapsed_time = 0

    while elapsed_time < 10:
        ret, frame = cap.read()
        
        cv2.imshow('Flow rack', frame)
        
        while (not ret) or (frame is None):
            ret, frame = cap.read()
            logger.error("Cannot read from webcam. Trying again.")

        frame_roi = cv2.bitwise_and(frame, frame, mask=camera_mask())
        gray = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2GRAY)

        if prvs is not None:
            flow = cv2.calcOpticalFlowFarneback(prvs, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])

            if np.mean(mag) > 0.4:
                logger.info("Movement detected!")
                time.sleep(abs(10-(time.time() - start_time)))
                return True

        prvs = gray
        elapsed_time = time.time() - start_time

    logger.info("No movement detected within 10 seconds.")
    return False