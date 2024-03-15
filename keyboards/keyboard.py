from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ add new tests"),
        ],
        [
            KeyboardButton(text="🎲 get random tests"),
        ],
    ],
    resize_keyboard=True,
)