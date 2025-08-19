from django.contrib import admin
from .models import Reservation, TimeSlot


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('date',)

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'is_booked')
    list_filter = ('date', 'is_booked')
    search_fields = ('date', 'time')