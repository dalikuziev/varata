import json
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "8863118900:AAH8NlAS7IqMf5Q4GSrDz2bUKAxdJJRP_Ak"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# aiogram handlerlaringizni shu yerga yoki alohida fayldan chaqirasiz
# @dp.message() ...

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            update = types.Update(**data)

            # Aiogram asinxron bo'lgani uchun event loop orqali ishlatiladi:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(dp.feed_update(bot, update))
            loop.close()

            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return HttpResponseForbidden()