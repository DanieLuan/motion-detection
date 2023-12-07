from Adafruit_IO import *
from loguru import logger

import time
import random
import cv2

from utils import is_movement_detected

port = 8883
ADAFRUIT_USERNAME = 'bren1n'
ADAFRUIT_KEY = 'aio_zrAL40J8aNkA58mccZfjWg3AqnwW'

FEED_NAME = 'flow-rack-movement'

def main():
    aio = None
    cap = cv2.VideoCapture(0)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while True:
        
        while aio is None:
            try:
                logger.info("Connecting to Adafruit IO...")
                aio = Client(ADAFRUIT_USERNAME, ADAFRUIT_KEY)
                logger.info("Connected to Adafruit IO!")
            except:
                logger.info("Could not connect to Adafruit IO.")
                time.sleep(10)

        start_time = time.time()
        
        logger.info(f"Detecting movement... {start_time}")
        
        data = 1 if is_movement_detected(0, cap, start_time) else 0
        
        logger.info(f"Movement detected: {data}")
        
        feed = aio.feeds(FEED_NAME)
        
        aio.send_data(feed.key, data)
        
        logger.info(f"{FEED_NAME}: send {data}")
        time.sleep(5)

if __name__ == "__main__":
    main()