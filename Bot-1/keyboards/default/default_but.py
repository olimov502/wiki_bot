from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

bolimlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Davlatlar🌏'),
            KeyboardButton(text='Mashhur shaxslar👨🏼‍💼'),

        ],
        [
            KeyboardButton(text='Hayvonot olami🦅'),
            KeyboardButton(text='Dunyo Brendlari💼')

        ],
        [
            KeyboardButton(text='Shaharlar🌆')
        ]
    ],
    resize_keyboard=True
)
