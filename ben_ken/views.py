from django.shortcuts import render
from django.views import generic
from .models import Booking


class Calendar_view(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_reference')
    template_name = 'index.html'
    paginate_by=8
