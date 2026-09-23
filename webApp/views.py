import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
import asyncio
from .handlers.users.start import rt as start
from .handlers.users.help import rt as help
from .handlers.users.button import rt as button
from .handlers.users.tugma import rt as tugma

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"
PROXY = "http://proxy.server:3128"
dp = Dispatcher()
bot = Bot(token=TOKEN)

dp.include_router(start)
dp.include_router(help)
dp.include_router(button)
dp.include_router(tugma)

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = types.Update(**json.loads(request.body))
        asyncio.run(dp.feed_update(bot, update))
        return HttpResponse("OK")
    return HttpResponse(status=405)
