from django.contrib import admin
from .models import Booking, Profile, Comment

admin.site.register(Profile)
admin.site.register(Booking)
admin.site.register(Comment)