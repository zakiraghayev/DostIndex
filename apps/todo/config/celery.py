import os
from celery import Celery
from django.conf import settings
from django.apps import apps

REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_VIRTUAL_HOST = os.environ.get("REDIS_VIRTUAL_HOST", "redis")
REDIS_VIRTUAL_PORT = os.environ.get("REDIS_VIRTUAL_PORT", "6379")


# Set default environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize Celery app
app = Celery('dost_index')

# Load configuration from Django settings
app.config_from_object(settings)

# Auto-discover tasks from all installed Django apps
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

# Update Celery configuration with Redis settings
app.conf.update(
    BROKER_URL=f'redis://:{REDIS_PASSWORD}@{REDIS_VIRTUAL_HOST}:{REDIS_VIRTUAL_PORT}/0',
    CELERY_RESULT_BACKEND=f'redis://:{REDIS_PASSWORD}@{REDIS_VIRTUAL_HOST}:{REDIS_VIRTUAL_PORT}/1',
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
)
