from django.urls import path
from . import views
# utils.py (例)
import datetime
from .models import TimeSlot

def create_daily_timeslots(date):
    start_hour = 10
    end_hour = 22
    for hour in range(start_hour, end_hour):
        time = datetime.time(hour=hour, minute=0)
        TimeSlot.objects.get_or_create(date=date, time=time)
urlpatterns = [
# reservation/urls.py
path('', views.reservation, name='reservation_from'),
path("api/timeslot-events/", views.timeslot_events, name="timeslot_events"),
path("api/available-timeslots/", views.available_timeslots, name="available_timeslots"),
]