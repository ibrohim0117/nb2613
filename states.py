from aiogram.fsm.state import State, StatesGroup


class AddCategory(StatesGroup):
    name = State()

class DeleteCategory(StatesGroup):
    name = State()

class UpdateCategory(StatesGroup):
    name = State()
    new_name = State()


class AddProduct(StatesGroup):
    name = State()
    price = State()
    image = State()
    category = State()


class ShowProduct(StatesGroup):
    name = State()