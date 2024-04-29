from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

@api_view(['GET', 'POST'])
def events(request):
    if request.method == 'GET':
        hotel_id = request.GET.get('hotel_id')
        updated__gte = request.GET.get('updated__gte')
        updated__lte = request.GET.get('updated__lte')
        rpg_status = request.GET.get('rpg_status')
        room_id = request.GET.get('room_id')
        night_of_stay__gte = request.GET.get('night_of_stay__gte')
        night_of_stay__lte = request.GET.get('night_of_stay__lte')

        events = Event.objects.all()

        if hotel_id:
            events = events.filter(hotel_id=hotel_id)
        if updated__gte:
            events = events.filter(timestamp__gte=updated__gte)
        if updated__lte:
            events = events.filter(timestamp__lte=updated__lte)
        if rpg_status:
            events = events.filter(rpg_status=rpg_status)
        if room_id:
            events = events.filter(room_id=room_id)
        if night_of_stay__gte:
            events = events.filter(night_of_stay__gte=night_of_stay__gte)
        if night_of_stay__lte:
            events = events.filter(night_of_stay__lte=night_of_stay__lte)

        serializer = EventSerializer(events, many=True)
        return Response({'events': serializer.data})

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)