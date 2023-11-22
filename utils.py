import os, json

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder as IB

from slugify import slugify

from keyboards.main_kb import main_back_keyboard_but




def find_files_courses(file_path='shop'):
    files = []
    for file in os.listdir(file_path):
        if file.endswith('.json'):
            files.append(os.path.join(file_path, file))
    
    return files

def decode_files_courses(files: list[str] ) -> list[dict]:
    files_courses = []
    for file in files:
        files_courses.append(
            json.load(
                open(file, encoding='utf-8')
                )
            )
    return files_courses

def generate_courses_kb(all_courses):
    courses_kb = IB()
    for course in all_courses:
        courses_kb.row(
            types.InlineKeyboardButton(
                text=course['name']
                , callback_data=f"course_{slugify(course['name'])}"
                )
            )
        # print(course['name'])
    courses_kb.row(main_back_keyboard_but)
    return courses_kb


if __name__ == '__main__':  
    print(find_files_courses())
    print(decode_files_courses(find_files_courses()))