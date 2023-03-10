from django import forms
from .models import Booking, Comment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields=(
            'email_address',
            'week_booking',
            'year_booking',
            'if_available',
            'number_of_o18',
            'number_of_u18',
            'number_of_pets',
            'contact_number',
            'additional_comment',)

class MakeComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('booking_reference','overall_comment','personal_comment','overall_feeling')
