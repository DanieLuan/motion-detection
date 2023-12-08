from telegram.ext import ApplicationBuilder, CommandHandler
import time
import datetime
import random
import cv2

from Adafruit_IO import *
from loguru import logger
from config import settings

from commands import start_detection, help

FEED_NAME = settings.FEED_NAME

def main():
    logger.info('Starting flow rack detection.')
    try:
        telegram_bot = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()
        logger.info('Bot instance created.')

    except Exception as e:    
        telegram_bot = None
        logger.error(f'An error occurred while creating the bot instance. {e}')
    
    if telegram_bot:
        try:
            logger.info("Adding commands to bot...")
            
            telegram_bot.add_handler(
                CommandHandler("help", help)
            )
            
            telegram_bot.add_handler(
                CommandHandler("start_detection", start_detection)
            )
            
        except Exception as e:
            logger.error(f'An error occurred while adding bot commands. {e}')

        logger.info("Starting bot...")
        telegram_bot.run_polling()
    
if __name__ == "__main__":
    main()