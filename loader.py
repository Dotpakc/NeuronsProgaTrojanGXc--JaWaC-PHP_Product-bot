from decouple import config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


API_TOKEN = config('TELEGRAM_API_TOKEN')
ADMIN_ID = config('TELEGRAM_ADMIN_ID')

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()