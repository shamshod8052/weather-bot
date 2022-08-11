from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Viloyat"),
            KeyboardButton(text="Joylashuv", request_location=True)
        ]
    ],
    resize_keyboard=True
)

viloyat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Buxoro"),
            KeyboardButton("Andijon"),
            KeyboardButton("Farg'ona")
        ],
        [
            KeyboardButton("Jizzax"),
            KeyboardButton("Urganch"),
            KeyboardButton("Namangan")
        ],
        [
            KeyboardButton("Navoiy"),
            KeyboardButton("Qarshi"),
            KeyboardButton("Samarqand")
        ],
        [
            KeyboardButton("Guliston"),
            KeyboardButton("Termiz"),
            KeyboardButton("Nurafshon")
        ],
        [
            KeyboardButton("Toshkent"),
            KeyboardButton("Nukus")
        ]
    ],
    resize_keyboard=True
)