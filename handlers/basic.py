from aiogram import Router,F,types
from aiogram.filters import Command


router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')
    
@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('Help!')