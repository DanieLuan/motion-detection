import cv2
import time
import numpy as np
from loguru import logger

def is_movement_detected(camera_id, cap, start_time):
    prvs = None
    elapsed_time = 0

    while elapsed_time < 10:
        ret, frame = cap.read()
        
        while (not ret) or (frame is None):
            ret, frame = cap.read()
            logger.error("Cannot read from webcam. Trying again.")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prvs is not None:
            flow = cv2.calcOpticalFlowFarneback(prvs, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])

            if np.mean(mag) > 0.4:
                logger.info("Movement detected!")
                return True

        prvs = gray
        elapsed_time = time.time() - start_time
        # logger.info(f"Elapsed time {elapsed_time} seconds")

    logger.info("No movement detected within 10 seconds.")
    return False