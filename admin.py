from aiogram import Router, types, F
from aiogram_i18n.context import I18nContext
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from datetime import datetime

from states import AddCategory, DeleteCategory, UpdateCategory, AddProduct, ShowProduct
from create import (
    insert_category, delete_category, read_category_detail,
    update_category, insert_product
)
from buttons.defoult import category_list_button, head_menu, admin_menu, product_list_button


dp = Router()


@dp.message(lambda message, i18n: message.text == i18n("add_category"))
async def a_ca(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("add_category_text"))
    await state.set_state(AddCategory.name)


# add cat
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

# - - - - - - - - - - - - - - - - - - - 
# add pro
@dp.message(lambda message, i18n: message.text == i18n("add_product"))
async def a_pro(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n('add_product_text'), reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddProduct.name)


@dp.message(AddProduct.name)
async def p_n(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Narxini yozing")    # i18 qilish kk
    await state.set_state(AddProduct.price)


@dp.message(AddProduct.price)
async def p_p(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(narxi=msg.text)
    await msg.answer("Rasmini yuboring")    # i18 qilish kk
    await state.set_state(AddProduct.image)


@dp.message(AddProduct.image, F.photo)
async def p_r(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(rasmi=msg.photo[-1].file_id)
    await msg.answer("Categoryni tanlang", reply_markup=category_list_button())    # i18 qilish kk
    await state.set_state(AddProduct.category)


@dp.message(AddProduct.category)
async def p_c(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(category=msg.text)
    data = await state.get_data()
    name = data.get('name')
    price = data.get('narxi')
    image = data.get('rasmi')
    category = data.get('category')
    time = datetime.now()
    insert_product(name, price, image, category, time)
    await msg.answer("OK", reply_markup=admin_menu(i18n))
    await state.clear()


# - - - - - - - - - - - - - - - - - - - 
# show pro

@dp.message(lambda message, i18n: message.text == i18n("show_product"))
async def sh_pro(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n('show_category'), reply_markup=category_list_button())
    await state.set_state(ShowProduct.name)


@dp.message(ShowProduct.name)
async def p_name_show(msg: types.Message, i18n: I18nContext, state: FSMContext):
    c_name = msg.text
    if read_category_detail(c_name):
        await msg.answer("Mavjud mahsulotlar", reply_markup=product_list_button(c_name))   # i18 kk
        await state.clear()
    else:
        await msg.answer("Category not found!")
        state.clear()











