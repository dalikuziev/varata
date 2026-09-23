from aiogram import Router, filters, types
rt = Router()

@rt.message()
async def aniqla(msg: types.Message):
    if msg.group_chat_created:
        print(msg.group_chat_created)
        await msg.answer("guruh yaratildi")
    elif msg.new_chat_members:
        print(msg.new_chat_members)
        ism = msg.new_chat_members[0].first_name
        await msg.answer(f"{ism} guruhga qo'shildi")

