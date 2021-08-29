import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "7717799"))
API_HASH = os.environ.get("API_HASH", "d6e0095d9f089d956ec3c298ca0471ba")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
ARQ_API_KEY = "MSZAYQ-IYVZRT-QELHBM-FISUKY-ARQ" 
LANGUAGE = os.environ.get("LANGUAGE", None)
ARQ_API_BASE_URL = "https://thearq.tech"

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
