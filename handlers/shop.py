from aiogram import Router,F,types
from aiogram.filters import Command


from keyboards.main_kb import main_keyboard, main_back_keyboard
from utils import (find_files_courses
                ,decode_files_courses
                ,generate_courses_kb
                )


router = Router()


@router.callback_query(F.data == 'courses')
async def courses(call: types.CallbackQuery):
    all_courses = decode_files_courses(find_files_courses())
    
    markup = generate_courses_kb(all_courses)
    
    await call.message.edit_text("Оберіть курс:"
                                ,reply_markup=markup.as_markup())
