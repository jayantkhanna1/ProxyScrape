from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proxy_scrape.settings')
# Create the Celery app
app = Celery('Proxy_scrape')
# Load the Celery config from the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# Discover tasks in all installed Django apps
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-every-afternoon': {
        'task': 'Scrapper.tasks.start_scraping',
        'schedule': crontab(hour=8, minute=0),
        'args': (),
    },
}

@app.task(bind=True)


def debug_task(self):
    print(f'Request: { self.request!r}') 
        