from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('details/', views.Customer_feedback.as_view(), name='details'),
    path('availability/', views.Availability.as_view(), name='check_avail'),
    path('booking/', views.Make_booking.as_view(), name='booking'),
]