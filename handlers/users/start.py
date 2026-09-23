from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message):
    await msg.answer("Labbay xo'jayin\nnima yordam beray?")
    await msg.answer("yordam kerak bo'lsa: /help")
