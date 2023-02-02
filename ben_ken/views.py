from django.shortcuts import render
from django.views import generic
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
    overall_comment = Comment.overall_comment
    overall_feeling = Comment.overall_feeling
    user = Comment.profile
    template_name = 'details.html'

class Calendar_view(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_reference')
    template_name = 'availability.html'
    paginate_by=8
    weeks = Booking.week_booking
    year = Booking.year_booking
    available = Booking.if_available

class Booking_form(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-week_booking','-year_booking')
    template_name = 'booking.html'
    weeks = Booking.week_booking
    year = Booking.year_booking


def weeks_view(request):
    weeks_view = Booking.objects.get('week_booking')
    year_view = Booking.objects.get('year_booking')
    template = loader.get_template('avaialbility.html')
    context = {
        'weeks_view': weeks_view,
        'years_view': year_view,
    }
    return HttpResponse(template.render(context, request))

    
