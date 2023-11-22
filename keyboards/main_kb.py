from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder as IB


#1.Курси
#2.Контакти
#3.Про нас
#4.Підтримка

main_keyboard = IB()
main_keyboard.row(types.InlineKeyboardButton(text="💻Курси", callback_data="courses"))  
main_keyboard.row(
    types.InlineKeyboardButton(text="🛒Мерчь", callback_data="merch")
    ,types.InlineKeyboardButton(text="📞Контакти", callback_data="contacts")
    ,types.InlineKeyboardButton(text="📝Про нас", callback_data="about")
    ,types.InlineKeyboardButton(text="📞Підтримка", callback_data="support")
    )


main_back_keyboard = IB()
main_back_keyboard_but =types.InlineKeyboardButton(text='👈 В головне меню', callback_data='main_back')
main_back_keyboard.row(main_back_keyboard_but)
