import asyncio
import logging
from aiogram.types import Message
from root import TOKEN
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import CommandStart
from buttons import menu

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hi !", reply_markup=menu)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
