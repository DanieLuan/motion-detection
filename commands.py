from telegram.ext import CallbackContext, Updater
import time
import datetime
import pandas as pd
import cv2

from Adafruit_IO import *
from loguru import logger
from config import settings

from src.utils import is_movement_detected
from src.adafruit import *

async def help(update, context):
    await context.bot.send_message(update.effective_chat.id, "Comandos disponíveis:\n/start_detection - Inicia a detecção de movimento.")
    
async def start_detection(update, context):  
    cap = cv2.VideoCapture(0)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    aio, feed = connect_on_adafruit()
    
    stop_count = 0
    
    send_report_time = time.time()
    
    await context.bot.send_message(update.effective_chat.id, f"Detecção de movimento das estações F e G iniciadas. Para mais informações acessar o dashboard: https://io.adafruit.com/bren1n/dashboards/flow-rack")

    while True:

        start_time = time.time()
        
        logger.info(f"Detecting movement...")
        
        data = 1 if is_movement_detected(cap, start_time) else 0
        
        logger.info(f"movement Status: {data}")
        
        timestamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        send_data_on_adafruit(aio, feed, data, timestamp)
        
        if data == 0:
            stop_count += 1
            if stop_count == 25:
                logger.info(f"Sending message to Telegram...")
                await context.bot.send_message(update.effective_chat.id, f"Atenção! Estação G e F estão paradas à mais de 5 minutos.")
                stop_count = 0
        else :
            stop_count = 0
            
        if time.time() - send_report_time > 600:
            logger.info(f"Sending last status to Telegram...")
            await context.bot.send_message(update.effective_chat.id, f"Último status: {last_status()}")
            send_report_time = time.time()
            
def last_status():
    csv = pd.read_csv('data.csv')
    
    if csv['status'].iloc[-1] == 1:
        return "Estações F e G em funcionamento."
    else:
        return "Estações F e G paradas."