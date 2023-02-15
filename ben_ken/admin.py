from django.contrib import admin
from .models import Booking, Profile, OverallComment

admin.site.register(Profile)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_reference','week_booking','year_booking',)
    list_filter = ('week_booking','year_booking')

admin.site.register(Booking, BookingAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('booking_reference_id','overall_feeling')
    list_filter = ('overall_feeling',)

admin.site.register(OverallComment, CommentAdmin)