from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from .models import Booking

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class Calendar_view(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_reference')
    template_name = 'details.html'
    paginate_by=8
    weeks = Booking.week_booking
    year = Booking.year_booking
    available = Booking.if_available


