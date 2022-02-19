from aiogram import types

from loader import dp
from keyboards.inline.inline_but import hayvonlar_but

# Echo bot
@dp.message_handler(text='Hayvonot olami🦅')
async def bot_echo(message: types.Message):
    await message.answer(text="Malumot olmoqchi bo'lgan brend nomini tanlang. "
                              "Yoki o'zingizga kerakli so'zni kiriting. ", reply_markup=hayvonlar_but)





