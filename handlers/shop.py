from aiogram import Router,F,types
from aiogram.filters import Command


from keyboards.main_kb import main_keyboard, main_back_keyboard
from utils import (find_files_courses
                ,decode_files_courses
                ,generate_courses_kb
                ,search_course_by_slug
                )

from slugify import slugify

router = Router()


@router.callback_query(F.data == 'courses')
async def courses_handler(call: types.CallbackQuery):
    all_courses = decode_files_courses(find_files_courses())
    
    markup = generate_courses_kb(all_courses)
    if call.message.photo:
        await call.message.answer("Оберіть курс:", reply_markup=markup.as_markup())
        await call.message.delete()
    else:
        await call.message.edit_text("Оберіть курс:", reply_markup=markup.as_markup())

@router.callback_query(F.data.startswith('course_'))
async def course_handler(call: types.CallbackQuery):
    slug = call.data.split('_')[-1]
    all_courses = decode_files_courses(find_files_courses())
    
    course = search_course_by_slug(slug, all_courses)
    
    image = types.FSInputFile(f"shop/img/{course['image']}")
    text = f"Назва курсу: {course['name']}\n\nОпис: {course['description']}\nОберіть рівень курсу:"
    markup = generate_courses_kb(course['products'],type=f'lvl_с_{slugify(course["name"])}_')
    

    await call.message.answer_photo(image, text, reply_markup=markup.as_markup())
    await call.message.delete()

@router.callback_query(F.data.startswith('lvl_с_'))
async def level_course_handler(call: types.CallbackQuery):
    slug_course = call.data.split('_')[-2]
    slug_level = call.data.split('_')[-1]
    all_courses = decode_files_courses(find_files_courses())
    
    course = search_course_by_slug(slug_course, all_courses)
    print(course)
    level = search_course_by_slug(slug_level, course['products'])
    
    image = types.FSInputFile(f"shop/img/{level['image']}")
    text = f"Назва курсу: {course['name']}\nРівень: {level['name']}\n\nОпис: {level['description']}\nОберіть дію:"
    
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Купити", url=level['link'])
            ],
            [
                types.InlineKeyboardButton(text="👈 Назад", callback_data=f"course_{slug_course}")
            ],
            [
                types.InlineKeyboardButton(text="👈 В головне меню", callback_data="main_back")
            ]
        ]
    )
    
    await call.message.answer_photo(image, text, reply_markup=markup)
    await call.message.delete()