import time
import datetime
import json

from Adafruit_IO import *
from loguru import logger

from config import settings

ADAFRUIT_USERNAME = settings.ADAFRUIT_USERNAME
ADAFRUIT_KEY = settings.ADAFRUIT_KEY
FEED_NAME = settings.FEED_NAME

def connect_on_adafruit():
    """Function to connect on Adafruit IO and return the Client and Feed objects.
    """
    aio, feed = None, None
    while aio is None:
            try:
                logger.info("Connecting to Adafruit IO...")
                aio = Client(ADAFRUIT_USERNAME, ADAFRUIT_KEY)
                logger.info("Connected to Adafruit IO!")
                feed = aio.feeds(FEED_NAME)
            except:
                logger.info("Could not connect to Adafruit IO.")
                time.sleep(10)
    return aio, feed

def send_data_on_adafruit(aio, feed, data, timestamp):
    """Function to send data to Adafruit IO.
    """
    aio.send_data(feed.key, data)

    logger.info(f"{FEED_NAME} - {timestamp} :: {data}")

    log_data = f"{timestamp},{data}"
    
    with open('data.csv', 'a') as f:
        f.write(log_data)
        f.write('\n')
        
        