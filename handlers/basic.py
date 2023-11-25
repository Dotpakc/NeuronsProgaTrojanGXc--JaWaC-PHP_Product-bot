from aiogram import Router,F,types
from aiogram.filters import Command


from keyboards.main_kb import main_keyboard,main_back_keyboard

router = Router()





@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.reply("Привіт!\n Я бот компанії Hillel IT School.\n Обери пункт меню 👇🏻"
                        ,reply_markup=main_keyboard.as_markup())
    

@router.callback_query(F.data == 'main_back')
async def main_back(call: types.CallbackQuery):
    if call.message.photo:
        await call.message.answer("Обери пункт меню 👇🏻",reply_markup=main_keyboard.as_markup())
        await call.message.delete()
    else:
        await call.message.edit_text("Обери пункт меню 👇🏻",reply_markup=main_keyboard.as_markup())


    
@router.callback_query(F.data == 'support')
async def support(call: types.CallbackQuery):
    await call.message.edit_text("Привіт! Служба підтримки компанії \"Hillel\".\nНапишіть своє питання:"
                      ,reply_markup=main_back_keyboard.as_markup())
    

@router.callback_query(F.data == 'contacts')
async def contacts(call: types.CallbackQuery):
    await call.message.edit_text("На всі ваші запитання дадуть відповідь адміністратори.\n"
                                 "📞Телефон: 0800 20 8020 безкоштовно по Україні\n"
                                 "📧Email:online@ithillel.ua\n"
    , reply_markup=main_back_keyboard.as_markup())
    
@router.callback_query(F.data == 'about')
async def about(call: types.CallbackQuery):
    await call.message.edit_text("Комп'ютерна школа Hillel — одна з найбільших IT-шкіл в Україні, і з кожним роком ми продовжуємо розвиватися і впроваджувати інновації у навчання."
                                "\n\nДо нас приходять і ті, хто хоче придбати нову професію або «прокачати» вже існуючі знання, і люди, які бажають підвищити свою кваліфікацію."
                                "\n\nОдним з ключових показників нашої роботи є відсоток працевлаштованих студентів. Для того, щоб цей показник був максимально високим, до викладацького складу ми запрошуємо тільки практикуючих фахівців з кращих IT-компаній, підбираємо корисні відеоматеріали і максимально комфортно організовуємо навчальний процес."
                                "\n\nЗнання допомагають змінювати життя на краще. Вчися заради мрії 🚀"
                                 , reply_markup=main_back_keyboard.as_markup())
    
@router.callback_query(F.data == 'merch')
async def merch(call: types.CallbackQuery):
    link_markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Перейти в магазин", url="https://gift.ithillel.ua/")
            ],
            [
                types.InlineKeyboardButton(text="👈 В головне меню", callback_data="main_back")
            ]
        ]
    )
    
    await call.message.edit_text("Вважаєте, що інвестиція в майбутнє — це найкращий подарунок? Ми теж 😉"
                                 "\n\nТому тепер у вас є можливість подарувати радість здобування нових навичок та професій вашій коханій людині, друзям або членам родини"
                                 "\n\nКнига це кращій подарунок, а курс у Комп'ютерній школі Hillel — найкорисніший ;) "
                                , reply_markup=link_markup)