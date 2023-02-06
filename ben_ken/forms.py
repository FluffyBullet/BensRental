from django import forms
from .models import Booking, Comment

class BookingForm(forms.Form):
    class Meta:
        model = Booking
        fields=('week_booking','year_booking','if_available')

class MakeComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('booking_reference','overall_comment','personal_comment','overall_feeling')