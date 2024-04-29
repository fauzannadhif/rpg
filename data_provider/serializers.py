from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'hotel_id', 'timestamp', 'rpg_status', 'room_id', 'night_of_stay']