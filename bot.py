import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set!")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🤖 سلام!\n\n"
        "به ربات اقتصاد مجازی خوش آمدی! 💰\n\n"
        "ربات با موفقیت راه‌اندازی شد ✅"
    )


async def main():
    bot = Bot(token=TOKEN)

    print("🤖 Bot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
