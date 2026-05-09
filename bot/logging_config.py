import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    # File mein log jayega
    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setLevel(logging.DEBUG)

    # Terminal pe bhi dikhega
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger