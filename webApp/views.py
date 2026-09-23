import json, asyncio, threading
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
dp.include_routers(start, help, button, tugma)

def process_update(data):
    """Xabarni orqa fonda qayta ishlash"""
    async def run():
        async with AiohttpSession(proxy=PROXY) as session:
            bot = Bot(token=TOKEN, session=session)
            update = types.Update(**data)
            await dp.feed_update(bot, update)
    asyncio.run(run())

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Telegram kutib qolmasligi uchun fon rejimida ishga tushiramiz:
            threading.Thread(target=process_update, args=(data,)).start()
            return HttpResponse("OK")  # Telegramga 0.01 soniyada javob qaytadi
        except Exception:
            return HttpResponse("OK")
    return HttpResponse(status=405)