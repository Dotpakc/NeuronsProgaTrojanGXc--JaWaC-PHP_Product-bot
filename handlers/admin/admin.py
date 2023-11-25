from aiogram import Router,F,types
from aiogram.filters import Command


from keyboards.main_kb import main_keyboard, main_back_keyboard
from keyboards.admin_kb import admin_main_keyboard, admin_back_keyboard
from utils import (find_files_courses
                ,decode_files_courses
                ,generate_courses_kb
                ,search_course_by_slug
                )

from slugify import slugify

ADMIN_LIST = [  # Список адмінів
            283941818,
            283941818,
]


router = Router()



@router.message(Command('admin'))
async def cmd_admin(message: types.Message):
    # if not message.from_user.id in ADMIN_LIST:
    #     return
    
    await message.answer("Вітаю, вас в адмін панелі!", reply_markup=admin_main_keyboard.as_markup())

