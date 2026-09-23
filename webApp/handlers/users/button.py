from aiogram import Router, filters, types
from keyboards.replyKeyboard.buttonKeyboard import button_keyboard
rt = Router()
@rt.message(filters.Command("button"))
async def button(msg: types.Message):
    n = "tugmalardan xohlaganingizni tanlang"
    await msg.answer(n, reply_markup=button_keyboard())

@rt.message()
async def b(msg: types.Message):
    if msg.users_shared:
        users = msg.users_shared.users
        for user in users:
            n = f"id: {user.user_id}\n"
            n += f"first_name: {user.first_name}\n"
            n += f"last_name: {user.last_name}\n"
            await msg.answer(n)


