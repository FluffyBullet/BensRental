from django.contrib import admin
from .models import Booking, Profile, Comment

admin.site.register(Profile)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_reference','week_booking','year_booking','user')
    list_filter = ('user','week_booking','year_booking')

admin.site.register(Booking, BookingAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','overall_feeling')
    list_filter = ('user','overall_feeling')

admin.site.register(Comment, CommentAdmin)