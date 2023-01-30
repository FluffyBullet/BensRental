from django import forms
from .models import Booking

class BookingForm(forms.Form):
    class Meta:
        model = Booking
        fields=('week_booking','year_booking','if_available')
