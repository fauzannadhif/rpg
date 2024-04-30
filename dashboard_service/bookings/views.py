import json

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Booking
from .serializers import BookingSerializer

class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        hotel_id = self.request.query_params.get('hotel_id')
        year = self.request.query_params.get('year')
        if hotel_id and year:
            queryset = queryset.filter(hotel_id=hotel_id, year=year)
        return queryset

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('hotel_id', openapi.IN_QUERY, description="ID of the hotel", type=openapi.TYPE_INTEGER),
        openapi.Parameter('year', openapi.IN_QUERY, description="The Year", type=openapi.TYPE_INTEGER),
        openapi.Parameter('period', openapi.IN_QUERY, description="Period of the bookings (month - monthly, day - daily)", type=openapi.TYPE_STRING),
    ])
    def get(self, request, *args, **kwargs):
        hotel_id = request.GET.get('hotel_id')
        year = request.GET.get('year')
        period = request.GET.get('period')

        if not year:
            return Response({'error': 'year is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not hotel_id:
            return Response({'error': 'hotel_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if period not in ['month', 'day']:
            return Response({'error': 'Invalid period. Need to be month or day.'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset())

        if period == "month":
            result = []
            for data in queryset:
                monthly_count = 0
                daily_bookings = json.loads(data.daily_bookings)
                for _, bookings in daily_bookings.items():
                    monthly_count += bookings
                result.append({"month": data.month, "no_of_bookings": monthly_count})

            return Response({"monthly_bookings": result})
        else:
            result = []
            for data in queryset:
                monthly_booking = []
                daily_bookings = json.loads(data.daily_bookings)
                for day, bookings in daily_bookings.items():
                    monthly_booking.append({"day": day, "no_of_bookings": bookings})
                result.append({"month": data.month, "bookings": monthly_booking})

            return Response({"daily_bookings": result})