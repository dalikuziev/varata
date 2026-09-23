import json
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"
PROXY = "http://proxy.server:3128"
dp = Dispatcher()

import asyncio
from aiogram import Dispatcher, Bot
from .handlers.users.start import rt as start
from .handlers.users.help import rt as help
from .handlers.users.button import rt as button
from .handlers.users.tugma import rt as tugma
from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message):
    await msg.answer("Labbay xo'jayin\nnima yordam beray?")
    await msg.answer("yordam kerak bo'lsa: /help")

dp.include_router(start)
dp.include_router(help)
dp.include_router(button)
dp.include_router(tugma)


@csrf_exempt
def telegram_webhook(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            update = types.Update(**data)

            async def handle_update():
                # Har bir so'rov uchun toza sessiya va bot nusxasi:
                session = AiohttpSession(proxy=PROXY)
                bot = Bot(token=TOKEN, session=session)
                try:
                    await dp.feed_update(bot, update)
                finally:
                    await session.close()

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(handle_update())
            loop.close()

            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return HttpResponseForbidden()
