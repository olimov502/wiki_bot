from aiogram import types

from loader import dp
from keyboards.inline.inline_but import brendlar_but

# Echo bot
@dp.message_handler(text='Dunyo Brendlari💼')
async def bot_echo(message: types.Message):
    await message.answer(text="Malumot olmoqchi bo'lgan hayvon nomini tanlang. "
                              "Yoki o'zingizga kerakli so'zni kiriting. ", reply_markup=brendlar_but)





