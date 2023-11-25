from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder as IB
# 1.🟢 Додати категорію курсів  🟡 Список категорій курсів  
# 2.🟢 Додати курс  🟡 Список курсів  🔴 Видалити курс
# 3.🟡 Список замовлень  
# 4.👈 Вийти з адмін меню


admin_main_keyboard = IB()

admin_main_keyboard.row(
    types.InlineKeyboardButton(text="🟢 Додати категорію курсів", callback_data="add_category")
    ,types.InlineKeyboardButton(text="🟡 Список категорій курсів", callback_data="list_category")
    )
admin_main_keyboard.row(    
    types.InlineKeyboardButton(text="🟢 Додати курс", callback_data="add_course")
    ,types.InlineKeyboardButton(text="🟡 Список курсів", callback_data="list_course")
    ,types.InlineKeyboardButton(text="🔴 Видалити курс", callback_data="del_course")
    )
admin_main_keyboard.row(
    types.InlineKeyboardButton(text="🟡 Список замовлень", callback_data="list_orders")
    )
admin_main_keyboard.row(
    types.InlineKeyboardButton(text="👈 Вийти з адмін меню", callback_data="main_back")
    )

admin_back_keyboard = IB()
admin_back_keyboard_but = types.InlineKeyboardButton(text='👈 В головне меню Адмін панелі', callback_data='admin_back')
admin_back_keyboard.row(admin_back_keyboard_but)
