from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *

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
    queryset = Booking.objects.order_by('booking_reference')


class Make_booking(generic.ListView):
    model = Booking
    template_name = 'booking.html'


    def post(self, request, *args, **kwargs):
        date_chosen = request.POST["week_selection"]
        _check_ref = str(date_chosen[:4]) + str(date_chosen[6:])
        queryset = Booking.objects.get(booking_reference=_check_ref)
        hire = queryset.charge
        _o18 = 0
        _u18 = 0
        _pets = 0

        if request.POST["adults"] != "":
            _o18 = request.POST["adults"]
        if request.POST["under_18"] != "" :
            _o18 = request.POST["under_18"]
        if request.POST["pets"] != "" :
            _o18 = request.POST["pets"]

        if queryset.if_available == True:
            e = Booking(
                booking_reference = _check_ref,
                booker = request.user,
                week_booking = date_chosen[6:],
                year_booking = date_chosen[:4],
                number_of_o18 = _o18,
                number_of_u18 = _u18,
                number_of_pets = _pets,
                provided_number = request.POST["contact_number"],
                additional_comment = request.POST["message"],
                charge = hire,
                if_available = False,
            )
            e.save()
            return render(request, 'availability.html')
        else:
            print("Already booked")
            return False




