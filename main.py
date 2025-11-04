import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types
from datetime import datetime

from admin import dp as admin

from create import create_db, insert_user, insert_category
from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from buttons.defoult import head_menu, language_button, admin_menu

ADMIN_ID = [1038185913, ]

TOKEN = "8471678376:AAH77m9WDN4p4TRrzFJhwf_xrmkb3-rJZls"
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
i18n_middleware.setup(dispatcher=dp)


@dp.message(Command('start'))
async def start(message: types.Message, i18n: I18nContext):
    await i18n.set_locale(message.from_user.language_code)
    full_name = message.from_user.full_name
    username = message.from_user.username
    tg_id = message.from_user.id
    # print(tg_id)
    if not insert_user(full_name, username, tg_id, datetime.now()):
        pass

    if message.from_user.id in ADMIN_ID:
        await message.answer(i18n("start_text"), reply_markup=admin_menu(i18n))

    else:
        await message.answer(i18n("start_text"), reply_markup=head_menu(i18n))


# change language step
@dp.message(lambda message, i18n: message.text == i18n("language_button"))
async def change_til(msg: types.Message, i18n: I18nContext):
    # await msg.answer(i18n("language_button"), reply_markup=)
    await msg.answer(i18n("k_til"), reply_markup=language_button(i18n))

# change uzb
@dp.message(lambda message, i18n: message.text == i18n("choose_language_text_uz"))
async def change_til_uz(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('uz')
    if msg.from_user.id in ADMIN_ID:
        await msg.answer(i18n("success_languange_text"), reply_markup=admin_menu(i18n))

    else:
        await msg.answer(i18n("success_languange_text"), reply_markup=head_menu(i18n))

# change ru
@dp.message(lambda message, i18n: message.text == i18n("choose_language_text_ru"))
async def change_til_ru(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('ru')
    if msg.from_user.id in ADMIN_ID:
        await msg.answer(i18n("success_languange_text"), reply_markup=admin_menu(i18n))

    else:
        await msg.answer(i18n("success_languange_text"), reply_markup=head_menu(i18n))

# change en
@dp.message(lambda message, i18n: message.text == i18n("choose_language_text_en"))
async def change_til_en(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('en')
    if msg.from_user.id in ADMIN_ID:
        await msg.answer(i18n("success_languange_text"), reply_markup=admin_menu(i18n))

    else:
        await msg.answer(i18n("success_languange_text"), reply_markup=head_menu(i18n))


async def main() -> None:
    create_db()
    dp.include_router(admin)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())