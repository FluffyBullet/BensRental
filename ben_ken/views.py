from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
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
    paginate_by = 20
    queryset = Booking.objects.order_by('booking_reference')

    def post(self, request, *args,**kwargs):
        new_year = request.POST["new_year"]
        new = Booking.objects.all()
        n = 1
        if new_year != Booking.year_booking:
            while n <= 53:
                new = Booking(
                    year_booking = new_year,
                    week_booking = n,  
                    booking_reference = str(new_year) + str("{:02d}".format(n)),
                    number_of_o18 = 0,
                    number_of_u18 = 0,
                    number_of_pets = 0,
                    if_available = "True",
                    charge = 185,
                    )
                new.save()
                n = n+1;
            messages.success = "Booking for " + new_year + "has been added!"
            return redirect('/availability', messages)
        elif new_year == 0:
            raise ValueError;
        else:
            raise ImportError;

    def delete(request):
        week = Booking.objects.get(Booking.booking_reference)
        week.delete()
        return HttpResponse(reverse('index)'))
    
    def update(request, booking_reference):
        stay = get_object_or_404(Booking, booking_reference = booking_reference)
        context = {
            'booking': stay,
        }
        updated = request.POST

        if request.method == "POST":
            update = Booking(
                booking_reference = stay.booking_reference,
                booker = stay.booker,
                week_booking = stay.week_booking,
                year_booking = stay.year_booking,
                number_of_o18 = updated["adults"], 
                number_of_u18 = updated["under_18"],
                number_of_pets = updated["pets"],
                provided_number = updated["contact_number"],
                additional_comment = updated["message"],
                charge = stay.hire,
                if_available = False,
            )
            update.save()
            return redirect('/availability')
        return render(request,'update_booking.html', context)


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

        
class My_visits(generic.ListView):
    model = Booking
    template_name = 'my_visits.html'
    paginate_by = 2

    def get(request):
        user= request.user.username
        queryset = Booking.objects.filter(booker=user).order_by('-booking_reference')
        context = {
            'visits' : queryset,
        }    
        return HttpResponse(context)

    @login_required
    def post(self, request, *args, **kwargs):
        print(request.POST["overall_comment"])
        stay = request.POST["overall_comment"]
        print(stay)
        user= request.user.username
        queryset = Booking.objects.filter(booker=user).order_by('-booking_reference')
        context = {
            'visits' : queryset,
        }
        c = Comment(
            booking_reference = stay,
            overall_comment = request.POST["overall_comment"],
            personal_comment = request.POST["personal_comment"],
            overall_feeling = request.POST["overall_feeling"],
        )
        c.save()

        return HttpResponse(context, 'my_visits.html')