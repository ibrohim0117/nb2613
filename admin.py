from aiogram import Router, types
from aiogram_i18n.context import I18nContext
from aiogram.fsm.context import FSMContext
from datetime import datetime

from states import AddCategory, DeleteCategory, UpdateCategory
from create import insert_category, delete_category, read_category_detail, update_category
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


# delete cat
@dp.message(lambda message, i18n: message.text == i18n("rm_category"))
async def a_ca(msg: types.Message, i18n: I18nContext, state: FSMContext):
    # await msg.answer(i18n("add_category_text"))   # uzilar qilasizlar
    await msg.answer("Tanlang", reply_markup=category_list_button())
    await state.set_state(DeleteCategory.name)


@dp.message(DeleteCategory.name)
async def d_c(msg: types.Message, state: FSMContext):
    c_name = msg.text
    if read_category_detail(c_name):
        delete_category(c_name)
        await msg.answer("Ok", reply_markup=category_list_button())
        await state.clear()
    else:
        await msg.answer("Category not found!")
        state.clear()



# update cat
@dp.message(lambda message, i18n: message.text == i18n("update_category"))
async def u_ca(msg: types.Message, i18n: I18nContext, state: FSMContext):
    # await msg.answer(i18n("add_category_text"))   # uzilar qilasizlar
    await msg.answer("Tanlang", reply_markup=category_list_button())
    await state.set_state(UpdateCategory.name)


@dp.message(UpdateCategory.name)
async def d_c(msg: types.Message, state: FSMContext):
    c_name = msg.text
    if read_category_detail(c_name):
        await state.update_data(old_name = c_name)
        await msg.answer("Yangi nom yozing")
        await state.set_state(UpdateCategory.new_name)
    else:
        await msg.answer("Category not found!", reply_markup=category_list_button())
        state.clear()


@dp.message(UpdateCategory.new_name)
async def d_c_n(msg: types.Message, state: FSMContext):
    n_name = msg.text
    date = await state.get_data()
    old_name = date.get('old_name')
    update_category(n_name, old_name)
    await msg.answer("Ok", reply_markup=category_list_button())
    await state.clear()



