from django.contrib import admin
from .models import Booking, Profile, Comment

admin.site.register(Profile)

admin.site.register(Comment)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_reference','week_booking','year_booking','user')
    list_filter = ('user','week_booking','year_booking')

admin.site.register(Booking, BookingAdmin)