from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (
    KeyboardButtonRequestUsers,
    KeyboardButtonRequestChat,
)
def button_keyboard():
    b = ReplyKeyboardBuilder()
    b.button(text="user", request_users=KeyboardButtonRequestUsers(
        request_id=1,
        user_is_bot=False,
        request_name=True,
        max_quantity=3
    ))
    b.button(text="bot", request_users=KeyboardButtonRequestUsers(
        request_id=2,
        user_is_bot=True,
    ))
    b.button(text="group", request_chat=KeyboardButtonRequestChat(
        request_id=3,
        chat_is_channel=False,
    ))
    b.button(text="channel", request_chat=KeyboardButtonRequestChat(
        request_id=4,
        chat_is_channel=True,
    ))
    b.adjust(2)
    return b.as_markup(resize_keyboard=True)

