from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def help(msg: types.Message):
    n = "bizda bor barcha kamandalar:\n"
    n += "/button\n"
    n += "/tugma\n"
    await msg.answer(n)
