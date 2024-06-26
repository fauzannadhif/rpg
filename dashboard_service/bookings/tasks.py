# tasks.py
import urllib.parse
import requests
import urllib
import json

from datetime import datetime, timedelta
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Booking

logger = get_task_logger(__name__)

@shared_task
def update_dashboard_data():
    # Fetch data from Data Provider
    now = datetime.now()
    update__gte = now - timedelta(minutes=1)
    update__lte = now
    params = {"updated__gte": update__gte, "updated__lte": update__lte}
    query_string = urllib.parse.urlencode(params)
    url = settings.DATA_PROVIDER_URL + "/events" + "?" + query_string
    data = requests.get(url).json()

    for event in data:
        hotel_id = event['hotel_id']
        timestamp = event['timestamp']
        date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').date()
        
        # Check if Booking entry exists for the hotel, year, and month
        try:
            booking = Booking.objects.get(hotel_id=hotel_id, year=date.year, month=date.month)
            daily_bookings = booking.daily_bookings
        except Booking.DoesNotExist:
            daily_bookings = json.dumps({})
            booking = Booking.objects.create(hotel_id=hotel_id, year=date.year, month=date.month, daily_bookings=daily_bookings)

        daily_bookings = json.loads(daily_bookings)

        # Update daily bookings
        day = str(date.day)
        daily_bookings[day] = daily_bookings.get(day, 0) + 1

        # Save updated dashboard data
        booking.daily_bookings = json.dumps(daily_bookings)
        booking.save()