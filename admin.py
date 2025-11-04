from aiogram import Router, types
from aiogram_i18n.context import I18nContext
from aiogram.fsm.context import FSMContext
from datetime import datetime

from states import AddCategory
from create import insert_category
from buttons.defoult import category_list_button


dp = Router()


@dp.message(lambda message, i18n: message.text == i18n("add_category"))
async def a_ca(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("add_category_text"))
    await state.set_state(AddCategory.name)


@dp.message(lambda message, i18n: message.text == i18n("show_category"))
async def l_ca(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n('show_category'), reply_markup=category_list_button())


@dp.message(AddCategory.name)
async def c_name(message: types.Message, i18n: I18nContext, state: FSMContext):
    name = message.text
    try:
        insert_category(name, datetime.now())
        await message.answer("ok")
        await state.clear()
    except:
        await message.answer("Bu nom band qayta urin!")
        await message.answer(i18n("add_category_text"))
        await state.set_state(AddCategory.name)



