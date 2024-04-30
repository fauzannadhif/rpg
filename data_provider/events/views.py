from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Event
from .serializers import EventSerializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        hotel_id = self.request.query_params.get('hotel_id')
        updated__gte = self.request.GET.get('updated__gte')
        updated__lte = self.request.GET.get('updated__lte')
        rpg_status = self.request.GET.get('rpg_status')
        room_id = self.request.GET.get('room_id')
        night_of_stay__gte = self.request.GET.get('night_of_stay__gte')
        night_of_stay__lte = self.request.GET.get('night_of_stay__lte')

        if hotel_id:
            queryset = queryset.filter(hotel_id=hotel_id)
        if updated__gte:
            queryset = queryset.filter(timestamp__gte=updated__gte)
        if updated__lte:
            queryset = queryset.filter(timestamp__lte=updated__lte)
        if rpg_status:
            queryset = queryset.filter(rpg_status=rpg_status)
        if room_id:
            queryset = queryset.filter(room_id=room_id)
        if night_of_stay__gte:
            queryset = queryset.filter(night_of_stay__gte=night_of_stay__gte)
        if night_of_stay__lte:
            queryset = queryset.filter(night_of_stay__lte=night_of_stay__lte)

        return queryset
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('hotel_id', openapi.IN_QUERY, description="ID of the hotel", type=openapi.TYPE_INTEGER),
        openapi.Parameter('updated__gte', openapi.IN_QUERY, description="Start date of the event", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        openapi.Parameter('updated__lte', openapi.IN_QUERY, description="End date of the event", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        openapi.Parameter('rpg_status', openapi.IN_QUERY, description="Status of the event (1 - booking, 2 - cancellation)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('room_id', openapi.IN_QUERY, description="ID of the room", type=openapi.TYPE_INTEGER),
        openapi.Parameter('night_of_stay__gte', openapi.IN_QUERY, description="Start date of stay", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        openapi.Parameter('night_of_stay__lte', openapi.IN_QUERY, description="End date of stay", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)