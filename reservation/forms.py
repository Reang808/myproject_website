from django import forms
from .models import Reservation
import datetime

class ReservationForm(forms.ModelForm):
    TIME_CHOICES = [(datetime.time(h, 0), f"{h:02d}:00") for h in range(10, 23)]
    time = forms.ChoiceField(choices=TIME_CHOICES, label="予約時間")

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }