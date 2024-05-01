from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Event


class EventListCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_event_create(self):
        url = reverse('events')

        data = {
            "hotel_id": 1,
            "timestamp": "2024-04-30T12:37:00Z",
            "rpg_status": 1,
            "room_id": 1,
            "night_of_stay": "2020-01-01"
        }


        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Event.objects.filter(hotel_id=1).exists())

    def test_event_list(self):
        url = reverse('events')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
