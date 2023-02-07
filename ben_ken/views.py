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
    print(model)
    def post(self, request, *args, **kwargs):
        date_chosen = request.POST["week_selection"]
        _check_ref = str(date_chosen[:4]) + str(date_chosen[6:])
        print(_check_ref)

        queryset = Booking.objects.get(booking_reference=_check_ref)
        print(queryset)

        if queryset.if_available == True:
            Booking.number_of_o18 = request.POST["adults"]
            Booking.additional_comment = request.POST["message"]
            print(request.POST["message"])
        else:
            print("Already booked")


        return HttpResponse(request, 'availability.html')



