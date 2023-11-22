from aiogram import Router,F,types
from aiogram.filters import Command


from keyboards.main_kb import main_keyboard, main_back_keyboard

router = Router()

@router.callback_query(F.data == 'courses')
async def courses(call: types.CallbackQuery):
    await call.message.edit_text("Оберіть курс:",reply_markup=main_back_keyboard.as_markup())
    