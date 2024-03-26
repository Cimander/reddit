import os
from celery import Celery

# Установка переменной окружения для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

# Создание экземпляра Celery
celery_app = Celery('reddit')

# Загрузка настроек из файла настроек Django
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Регистрация задач из всех приложений Django
celery_app.autodiscover_tasks()