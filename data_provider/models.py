from django.db import models

class Event(models.Model):
    BOOKING = 1
    CANCELLATION = 2
    RPG_STATUS_CHOICES = [
        (BOOKING, 'Booking'),
        (CANCELLATION, 'Cancellation'),
    ]

    id = models.AutoField(primary_key=True)
    hotel_id = models.IntegerField()
    timestamp = models.DateTimeField()
    rpg_status = models.IntegerField(choices=RPG_STATUS_CHOICES)
    room_id = models.IntegerField()
    night_of_stay = models.DateField()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Event {self.id} - Hotel {self.hotel_id} - {self.get_rpg_status_display()}"