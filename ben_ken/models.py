from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0,"Display"),(1,"Hide"))


class Profile(models.Model):
    profile_reference = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    user_id = models.ForeignKey(User, to_field="username", on_delete=models.DO_NOTHING)
    contact_number = models.CharField(max_length=11, blank=False)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    address_line_3 = models.CharField(max_length=50)
    address_line_4 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=7)
    phone = "phone"
    email = "email"
    post = "post"
    preference_of_contact = models.CharField(max_length=6,choices=(
        (phone,"Phone"),
        (post, "Post"),
        (post, "letter"),
    ))
    admin_comments = models.CharField(max_length=250, blank=True)
      
    def __str__(self):
        return self.user_id.username


class Booking(models.Model):
    booking_reference = models.IntegerField(unique=True, primary_key=True, null=False)
    booker = models.ForeignKey(User, to_field="username", on_delete=models.DO_NOTHING,blank=True, null=True)
    week_booking = models.SmallIntegerField()
    year_booking = models.SmallIntegerField()
    if_available = models.BooleanField(default=True)
    number_of_o18 = models.SmallIntegerField(default=0)
    number_of_u18 = models.SmallIntegerField(default=0)
    number_of_pets = models.SmallIntegerField(default=0)
    charge = models.PositiveSmallIntegerField(null=True)
    additional_comment = models.TextField(blank=True, null=True)
    provided_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return "Booking reference: " + str(self.booking_reference)
 

class OverallComment(models.Model):
    o_comment_id = models.AutoField(primary_key=True, unique=True)
    booking_reference = models.ForeignKey(Booking, to_field='booking_reference', on_delete=models.CASCADE)
    overall_comment = models.CharField(max_length=250)
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

    def __int__(self):
        return self.o_comment_id

    def __str__(self):
        return "comment" + str(self.o_comment_id) + "by" + str(self.booking_reference.booker) 
    
class PersonalComment(models.Model):
    p_comment_id = models.AutoField(primary_key=True, unique=True)
    booking_reference = models.ForeignKey(Booking, to_field='booking_reference', on_delete=models.CASCADE)
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

    def __int__(self):
        return self.p_comment_id

    def __str__(self):
        return "comment" + str(self.p_comment_id) + "by" + str(self.booking_reference.booker) 