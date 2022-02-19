from aiogram import types

from aiogram.types import ContentType, InputFile

from loader import dp
from loader import bot

# Echo bot
@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    rasm_id = message.photo[-1].file_id

    await message.answer(text=f'{rasm_id}')



