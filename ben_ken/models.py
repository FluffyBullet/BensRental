from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0,"Display"),(1,"Hide"))

class Account(models.Model):
   user_reference = models.SlugField(primary_key=True, unique=True)
   first_name = models.CharField(max_length=15)
   last_name = models.CharField(max_length=25)
   contact_number = models.IntegerField()
   address_line_1 = models.CharField(max_length=200)
   address_line_2 = models.CharField(max_length=200)
   address_line_3 = models.CharField(max_length=200)
   address_line_4 = models.CharField(max_length=200)
   post_code = models.CharField(max_length=9)
   email_address = models.EmailField(max_length=254)
   preference_of_contact = models.CharField(max_length=30)
   admin_comment = models.TextField()


class Booking(models.Model):
    booking_reference = models.SmallAutoField(primary_key=True, unique=True)
    account_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_o18 = models.PositiveSmallIntegerField()
    number_of_u18 = models.PositiveSmallIntegerField()
    number_of_pets = models.PositiveSmallIntegerField()
    total_guest = models.PositiveSmallIntegerField()

class Comment(models.Model):
    comment_reference = models.SlugField(primary_key=True, unique=True)
    user_reference = models.ForeignKey(Account, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    overall_comment = models.CharField(max_length=200, choices=STATUS, default=0)
    personal_comment = models.CharField(max_length=200, choices=STATUS, default=0)

class Task(models.Model):
    taks_reference = models.IntegerField(primary_key=True)
    user_name = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    booking_reference = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # start_date = models.ForeignKey(Booking.start_date,on_delete=models.CASCADE)
    # end_date = models.ForeignKey(Booking.end_date, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=200)
    task_complete = models.BooleanField(default=False)

class Messages(models.Model):
    messages_thread = models.IntegerField(primary_key=True)
    # messages_from = models.ForeignKey(Account, on_delete=models.CASCADE)
    # messages_to = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    message_header = models.CharField(max_length=50)
    message_text = models.TextField()
    report = models.BooleanField(default=False)
