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

    dashboard_data = Booking.objects.filter(hotel_id=hotel_id, year=year)

    if period == "month":
        monthly_bookings = []
        for data in dashboard_data:
            monthly_count = 0
            daily_bookings = json.loads(data.daily_bookings)
            for _, bookings in daily_bookings.items():
                monthly_count += bookings
            monthly_bookings.append({"month": data.month, "bookings": monthly_count})

        return Response({"monthly_bookings": monthly_bookings})
    else:
        daily_bookings = []
        for data in dashboard_data:
            daily_bookings = json.loads(data.daily_bookings)
            for day, bookings in daily_bookings.items():
                daily_bookings.append({"month": data.month, "day": day, "bookings": bookings})

        return Response({"daily_bookings": monthly_bookings})