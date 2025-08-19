from django import forms
from .models import Reservation
import datetime


class ReservationForm(forms.ModelForm):


    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }