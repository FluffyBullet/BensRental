from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import BookingForm

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class Customer_feedback(generic.ListView):
    model= Comment
    queryset = Comment.objects.order_by('-comment_id')
    paginate_by = 4
    template_name = 'details.html'

class Availability(generic.ListView):
    model = Booking
    template_name = 'availability.html'
    paginate_by = 8


class Make_booking(generic.ListView):
    model = Booking
    template_name = 'booking.html'

    def post(self, request, *args, **kwargs):
        req_booking = BookingForm(data=request.POST)
        _req_ref = str(req_booking.week_requested)+ str(req_booking.year_requested)
        queryset = Booking.objects.filter(booking_reference = _req_ref)
        if req_booking.is_valid():
            print(req_booking)
            if queryset == True:
                print("It works, Huzah!")
            return HttpResponse(request, 'availability.html')

