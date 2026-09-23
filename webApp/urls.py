from django.urls import path
from .views import telegram_webhook

urlpatterns = [
    # boshqa yo'llar...
    path('api/telegram-webhook/', telegram_webhook, name='telegram_webhook'),
]

