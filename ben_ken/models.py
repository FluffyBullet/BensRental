from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0,"Display"),(1,"Hide"))

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=11, blank=False)
    address_line_1 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=7)
      
    def __str__(self):
        return self.user

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    booking_reference = models.AutoField(unique=True, primary_key=True)
    week_booking = models.SmallIntegerField()
    year_booking = models.SmallIntegerField()
    calendar_reference = models.SmallIntegerField(unique=True)
    number_of_o18 = models.SmallIntegerField(blank=False)
    number_of_u18 = models.SmallIntegerField(blank=False)
    number_of_pets = models.SmallIntegerField(blank=False)
