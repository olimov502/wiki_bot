from aiogram import types

from loader import dp
from keyboards.inline.inline_but import davlatlar_but

# Echo bot
@dp.message_handler(text='Davlatlar🌏')
async def bot_echo(message: types.Message):
    await message.answer(text="Davlatlar bo'limidan kerakli davlat nomini "
                              "tanlang. Yoki o'zingiz davlat nomini kiriting. ", reply_markup=davlatlar_but)





