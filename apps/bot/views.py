from django.core.management.base import BaseCommand
from telegram.ext import Updater
from blog import settings

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN

class Command(BaseCommand):
    help = 'Запуск Telegram бота'

    def handle(self, *args, **kwargs):
        updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

        updater.start_polling()
        updater.idle()