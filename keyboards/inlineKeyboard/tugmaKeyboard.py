from aiogram.utils.keyboard import InlineKeyboardBuilder
def tugma():
    b = InlineKeyboardBuilder()
    b.button(text="oddiy", callback_data="nima gap")
    b.adjust(2)
    return b.as_markup(resize_keyboard=True)
def cars():
    b = InlineKeyboardBuilder()
    mashinalar = ["cobalt", "matiz", "tiko", "damas"]
    for i in mashinalar:
        b.button(text=i, callback_data="rang")
    b.adjust(2)
    return b.as_markup()
def colors():
    b = InlineKeyboardBuilder()
    ranglar = ["qora", "oq", "qizil"]
    for i in ranglar:
        b.button(text=i, callback_data="olindi")
    b.adjust(2)
    return b.as_markup()
