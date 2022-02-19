from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_but import bolimlar_buttons
from loader import dp,baza
from keyboards.inline.inline_but import davlatlar_but
import datetime
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    username = message.from_user.username
    tg_id = message.from_user.id
    vaqt = datetime.datetime.now()
    baza.user_qoshish(ismi=ism,username=username,tg_id=tg_id,vaqt=vaqt)

    await message.answer(f"Salom, {message.from_user.full_name}   Wiki botga hush kelibsiz."
                         f"Bo'limlardan birini tanlang yoki o'zingizga kerakli so'zni kiriting!", reply_markup=bolimlar_buttons)
