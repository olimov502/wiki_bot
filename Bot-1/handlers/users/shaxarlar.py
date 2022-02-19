from aiogram import types

from loader import dp
from keyboards.inline.inline_but import shaxarlar_but

# Echo bot
@dp.message_handler(text='Shaharlar🌆')
async def bot_echo(message: types.Message):
    await message.answer(text="Malumot olmoqchi bo'lgan shahar nomini tanlang. "
                              "Yoki o'zingizga kerakli so'zni kiriting. ", reply_markup=shaxarlar_but)





