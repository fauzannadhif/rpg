import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Booking


class BookingListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Booking.objects.create(hotel_id=1, year=2024, month=5, daily_bookings=json.dumps({"1": 1, "2": 2}))

    def test_booking_list_monthly(self):
        url = "%s?year=2024&hotel_id=1&period=month" % (reverse("dashboards"))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_body = response.json()
        monthly_booking = response_body.get("monthly_bookings", [])
        self.assertEqual(len(monthly_booking), 1)
    
    def test_booking_list_daily(self):
        url = "%s?year=2024&hotel_id=1&period=day" % (reverse("dashboards"))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_body = response.json()
        daily_booking = response_body.get("daily_bookings", [])
        self.assertEqual(len(daily_booking), 1)
        self.assertEqual(len(daily_booking[0]["bookings"]), 2)
