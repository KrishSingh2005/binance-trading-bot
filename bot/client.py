import os
import hmac
import hashlib
import time
import requests
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

TESTNET_BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    api_key = os.getenv("BINANCE_API_KEY", "").strip()
    api_secret = os.getenv("BINANCE_API_SECRET", "").strip()

    if not api_key or not api_secret:
        raise ValueError("API keys missing hain .env mein")

    logger.info("Binance Testnet se successfully connect ho gaye!")
    return {"api_key": api_key, "api_secret": api_secret}