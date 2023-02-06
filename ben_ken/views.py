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

    def post(request):
        if request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
            return render(Availability)
        return HttpResponse('availability.html')
    

