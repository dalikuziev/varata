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
    try:
        async def run():
            async with AiohttpSession(proxy=PROXY) as session:
                bot = Bot(token=TOKEN, session=session)
                update = types.Update(**data)
                await dp.feed_update(bot, update)
        asyncio.run(run())
    except Exception as e:
        print(f"Update error: {e}")

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            threading.Thread(target=process_update, args=(data,)).start()
        except Exception as e:
            print(f"Request error: {e}")
        return HttpResponse("OK")  # Har doim 200 qaytaradi, Telegram 502 olmaydi
    return HttpResponse("Method not allowed", status=405)