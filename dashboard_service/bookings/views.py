import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking

@api_view(['GET'])
def get_dashboard(request):
    hotel_id = request.GET.get('hotel_id')
    year = request.GET.get('year')
    period = request.GET.get('period')
    if period not in ['month', 'day']:
        return Response({'error': 'Invalid period. Need to be month or day.'}, status=status.HTTP_400_BAD_REQUEST)
    if not year:
        return Response({'error': 'year is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not hotel_id:
        return Response({'error': 'hotel_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    dashboard_data = Booking.objects.filter(hotel_id=hotel_id, year=year)

    if period == "month":
        result = []
        for data in dashboard_data:
            monthly_count = 0
            daily_bookings = json.loads(data.daily_bookings)
            for _, bookings in daily_bookings.items():
                monthly_count += bookings
            result.append({"month": data.month, "no_of_bookings": monthly_count})

        return Response({"monthly_bookings": result})
    else:
        result = []
        for data in dashboard_data:
            monthly_booking = []
            daily_bookings = json.loads(data.daily_bookings)
            for day, bookings in daily_bookings.items():
                monthly_booking.append({"day": day, "no_of_bookings": bookings})
            result.append({"month": data.month, "bookings": monthly_booking})

        return Response({"daily_bookings": result})