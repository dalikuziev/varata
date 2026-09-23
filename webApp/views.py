import asyncio
import json
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"

# PythonAnywhere Free tarifi uchun majburiy Proxy sozlamasi:
session = AiohttpSession(proxy="http://proxy.server:3128")
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

# --- HANDLERLAR ---
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Qabul qilindi: {message.text}")
# ------------------

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            update = types.Update(**data)

            # Asinxron ishni to'g'ri yakunlash:
            async def process():
                await dp.feed_update(bot, update)
                await session.close()  # Sessiyani tozalash qotib qolishning oldini oladi

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(process())
            loop.close()

            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return HttpResponseForbidden()