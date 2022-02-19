from aiogram import types

from loader import dp
from keyboards.inline.inline_but import shaxslar_but

# Echo bot
@dp.message_handler(text='Mashhur shaxslar👨🏼‍💼')
async def bot_echo(message: types.Message):
    await message.answer(text="Kerakli ismni tanlang."
                              "Yoki o'zingiz ism kiriting. ", reply_markup=shaxslar_but)
