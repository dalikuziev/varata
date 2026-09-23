import json
import asyncio
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"
PROXY = "http://proxy.server:3128"

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