from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingListAPIView.as_view(), name='dashboards'),
]