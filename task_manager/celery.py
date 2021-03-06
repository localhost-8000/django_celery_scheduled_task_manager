import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

app = Celery("task_manager")
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-task-report-to-user": {
        'task': 'send_periodic_reportes_to_user',
        'schedule': crontab(minute='*/15'),
    }
}
