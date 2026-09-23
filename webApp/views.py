import json, asyncio
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession

from .handlers.users.start import rt as start
from .handlers.users.help import rt as help
from .handlers.users.button import rt as button
from .handlers.users.tugma import rt as tugma

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"
PROXY = "http://proxy.server:3128"

dp = Dispatcher()
dp.include_routers(start, help, button, tugma)  # Barchasini bitta qatorda ulash mumkin


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        async def process():
            # Har bir so'rov uchun alohida sessiya va bot ochiladi:
            async with AiohttpSession(proxy=PROXY) as session:
                bot = Bot(token=TOKEN, session=session)
                update = types.Update(**json.loads(request.body))
                await dp.feed_update(bot, update)

        asyncio.run(process())
        return HttpResponse("OK")
    return HttpResponse(status=405)

