from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
            _u18 = request.POST["under_18"]

        if request.POST["pets"] != "" :
            _pets = request.POST["pets"]

        print("Over18 = " + str(_o18))
        print("Under18 = " + str(_u18))
        print("pets = " + str(_pets))

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
            messages.success(request,"Thank you for your booking, this has been processed.")
            return redirect('/availability', messages)
        else:
            messages.warning(request,"This week has already been booked, please select another week.")
            return redirect('/booking',messages)
        
class my_visits(generic.ListView):
    model = Booking
    template_name = 'my_visits.html'

    @login_required
    def populate_list(self, request):
        user= request.user.username
        template = loader.get_template('my_visits.html')
        queryset = Booking.objects.filter('booker'==user)
        return render(request, 'my_visits.html',{
            "user":user,
            "visit":queryset,

        })

