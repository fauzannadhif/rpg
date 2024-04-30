# tasks.py
import requests
import random

from datetime import datetime
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@shared_task
def send_event():
    # Fetch data from Data Provider
    now = datetime.now().replace(microsecond=0)
    date = now.date()
    
    url = settings.DATA_PROVIDER_URL + "/events/"
    for _ in range(random.randint(1, 5)):
        body = {
            "hotel_id": 1,
            "timestamp": now,
            "rpg_status": 1,
            "room_id": random.randint(1, 100),
            "night_of_stay": str(date.year) + "-" + str(date.month) + "-" + str(date.day)
        }
        data = requests.post(url, data=body).json()
