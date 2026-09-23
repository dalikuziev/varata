import json
import asyncio
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"
PROXY = "http://proxy.server:3128"


import asyncio
from aiogram import Dispatcher, Bot
from handlers.users.start import rt as start
from handlers.users.help import rt as help
from handlers.users.button import rt as button
from handlers.users.tugma import rt as tugma
from handlers.groups.aniqlaGroup import rt as aniqlaGroup
dp = Dispatcher()
async def main():
    bot = Bot(TOKEN)
    dp.include_router(start)
    dp.include_router(help)
    # dp.include_router(aniqlaGroup)
    dp.include_router(tugma)
    dp.include_router(button)
    await dp.start_polling(bot)
if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())

