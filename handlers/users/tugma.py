from aiogram import Router, types, filters, F
from keyboards.inlineKeyboard.tugmaKeyboard import tugma, cars, colors
rt = Router()
@rt.message(filters.Command("tugma"))
async def button(msg: types.Message):
    n = "shaffof tugmalardan birini tanlang"
    await msg.answer(n, reply_markup=tugma())
@rt.callback_query(F.data == "nima gap")
async def button(callback: types.CallbackQuery):
    await callback.answer("juda yaxshi")
    await callback.message.edit_text("mashinalardan birini tanlang", reply_markup=cars())
@rt.callback_query(F.data == "rang")
async def button(callback: types.CallbackQuery):
    await callback.answer("mashina muvaffaqqiyatli tanlandi!")
    await callback.message.edit_text("mashina uchun rang tanlang!", reply_markup=colors())
@rt.callback_query(F.data == "olindi")
async def button(callback: types.CallbackQuery):
    await callback.answer("rangni ham vapshe zo'rini tanladingiz")
    await callback.message.edit_text("mazza qilib ming!!!")
