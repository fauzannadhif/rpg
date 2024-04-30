from django.db import models

class Booking(models.Model):
    hotel_id = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    daily_bookings = models.TextField()  # JSON field to store daily booking data

    def __str__(self):
        return f"Booking for Hotel {self.hotel_id}, Year {self.year}, Month {self.month}"