# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_service.settings')

app = Celery('dashboard_service')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Define queues
app.conf.task_queues = {
    'update_dashboard_topic': {
        'exchange': 'update_dashboard_topic',
        'routing_key': 'update_dashboard_topic',
    },
}

# Define routing rules
app.conf.task_routes = {
    'bookings.tasks.update_dashboard_data': {'queue': 'update_dashboard_topic'},
}

# Configure RabbitMQ broker URL
app.conf.broker_url = f'amqp://{settings.RABBITMQ_USERNAME}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}/'