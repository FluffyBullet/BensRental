from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main , name='home'),
    path('details/', views.Customer_feedback.as_view(), name='details'),
    path('availability/', views.Availability.as_view(), name='check_avail'),
    path('booking/', views.Make_booking.as_view(), name='make_booking'),
    path('my_visits/', views.My_visits.as_view(), name='my_visits'),
    path('update_booking/<int:booking_reference>', views.Availability.update , name="update_booking"),
    path('cancel_booking/<int:booking_reference>', views.Availability.cancel, name="cancel_booking"),
    path('accounts/', include('allauth.urls')),
]