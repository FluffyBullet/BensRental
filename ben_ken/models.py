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
    if_available = models.BooleanField(default=True)
    number_of_o18 = models.SmallIntegerField(blank=False)
    number_of_u18 = models.SmallIntegerField(blank=False)
    number_of_pets = models.SmallIntegerField(blank=False)
 

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    overall_comment = models.CharField(max_length=250)
    personal_comment = models.CharField(max_length=250)
    happy ="Happy"
    indifferent = "Indifferent"
    unhappy ="Unhappy"

    overall_feeling = models.CharField(max_length=11,
        choices=(
        (happy, "Happy"),
        (indifferent, "Indifferent"),
        (unhappy, "Unhappy"),
        )
    )