from django.contrib.auth.models import AbstractUser
from django.db import models

class Donor(models.Model):
    donor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=100, null=False, default= '')
    phone_num = models.CharField (max_length=15, null=True)
    email = models.EmailField(blank=False)
    gender_choices = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('Others', 'others')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    age = models.PositiveIntegerField (blank=False)
    blood_type = models.CharField(max_length=10, null=True)

    class Meta:
         verbose_name = "Donor"

    def __str__(self):
        return self.first_name

class Staff(AbstractUser):
    address = models.CharField(max_length=100, null=False, default= '')
    name = models.CharField(max_length=30, null=False, default= '')
    phone_num = models.CharField (max_length=15, null=True)
    gender_choices = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('Others', 'others')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    salary = models.DecimalField (decimal_places=2, max_digits=7, null=True)
    description = models.CharField (max_length=100, null=True)
    class Meta:
         verbose_name = "Staff"
         verbose_name_plural = "Staff"

    def __str__(self):
        return self.first_name

class Recipient(models.Model):
    recipient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    mobile_num = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=100, null=False, default= '')
    blood_type = models.CharField(max_length=10, null=True)
    units_requested = models.CharField(max_length=4)
    date_of_request = models.DateField (blank=True, null=True)
    date_of_accepted = models.DateField (blank=True, null=True)

    class Meta:
         verbose_name = "Recipient"

    def __str__(self):
        return self.name
