from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0,"Display"),(1,"Hide"))

class Account(models.Model):
   user_reference = models.SlugField(unique=True)
   first_name = models.CharField(max_length=15)
   last_name = models.CharField(max_length=25)
   contact_number = models.IntegerField(max_length=12)
   address_line_1 = models.CharField(max_length=200)
   address_line_2 = models.CharField(max_length=200)
   address_line_3 = models.CharField(max_length=200)
   address_line_4 = models.CharField(max_length=200)
   post_code = models.CharField(max_length=9)
   email_address = models.EmailField(max_length=254)
   preference_of_contact = models.CharField()

   
class Comment(models.Model):


class Booking(models.Model):


class Task(models.Model):


class Messages(models.Model):

