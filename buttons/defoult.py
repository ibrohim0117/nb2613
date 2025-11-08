from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext

from create import read_category, read_product


def language_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('choose_language_text_uz')),
                KeyboardButton(text=_('choose_language_text_ru')),
                KeyboardButton(text=_('choose_language_text_en'))
            ]
        ],
        resize_keyboard=True
    )



def head_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('main_menyu'))
            ],

            [
                KeyboardButton(text=i18n('about_me')),
                KeyboardButton(text=_('contact_me'))
            ],
            
            [
                KeyboardButton(text=_('language_button')),
            ]
        ],
        resize_keyboard=True
    )


def admin_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                # kategory button
                KeyboardButton(text=_('show_category'))
            ],

            [
                KeyboardButton(text=i18n('add_category')),
                KeyboardButton(text=_('rm_category')),
                KeyboardButton(text=_('update_category')),
            ],

            [
                # product button
                KeyboardButton(text=_('show_product'))
            ],

            [
                KeyboardButton(text=i18n('add_product')),
                KeyboardButton(text=_('rm_product')),
                KeyboardButton(text=_('update_product')),
            ],
            
            [
                KeyboardButton(text=_('language_button')),
            ]
        ],
        resize_keyboard=True
    )



def category_list_button():
    categories = read_category()
    
    buttons = [
        [KeyboardButton(text=name[0])] for name in categories
    ]
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return keyboard


def product_list_button(category):
    products = read_product(category)
    print(products)

    if products:
        buttons = [
            [KeyboardButton(text=name[0])] for name in products
        ]
    else:
        buttons = [
            [KeyboardButton(text="Chiqish🔙")]
        ]
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return keyboard



