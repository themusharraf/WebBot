from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

btn = [
    [KeyboardButton(text="Register", web_app=WebAppInfo(url="https://themusharraf.github.io/"))]
]
menu = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)
