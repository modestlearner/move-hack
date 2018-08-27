import re
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager, PermissionsMixin, User
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

from yatri import settings


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# Create your models here.
class Todo(models.Model):
    destination = models.CharField(max_length=1000)
    source = models.CharField(max_length=100)
    escore = models.CharField(blank=True,max_length=10)
    type = models.CharField(max_length=100)
    user_choices = (('Petrol Electric', 'Petrol Electric'), ('Diesel Electric', 'Diesel Electric'), ('Hybrid', 'Hybrid'), ('Petrol', 'Petrol'),('Diesel','Diesel'))
    types = models.CharField(_('vehicle type'), max_length=30, blank=False, choices=user_choices)







    def save(self,*args,**kwargs):

        if self.escore is None or self.escore == '' or self.escore == 0.0:
            if self.types == "Diesel":
                self.escore = 3.72
            if self.type == "Petrol":
                self.escore = 5.07
            if self.types == "Petrol Electric":
                self.escore = 2.83
            if self.types == "Diesel Electric":
                self.escore = 3.54
            if self.types =="Hybrid":
                self.escore = 4.0
        super(Todo, self).save(*args, **kwargs)
    def __str__(self):
        return self.destination


class Vehicle(models.Model):
    year = models.IntegerField(_('year of purchase'), blank=False)
    make = models.CharField(_('vehicle make'), max_length=254, blank=False)
    plate = models.CharField(_('liscenced plate number'), max_length=10, blank=False)
    model = models.CharField(_('vehicle model'), max_length=254, blank=False)
    user_choices = (('Petrol Electric', 'Petrol Electric'), ('Diesel Electric', 'Diesel Electric'), ('Hybrid', 'Hybrid'), ('Petrol', 'Petrol'),('Diesel','Diesel'))
    type = models.CharField(_('vehicle type'), max_length=30, blank=False, choices=user_choices)


    def __str__(self):
        return self.plate


class Aadhar(models.Model):
    aadhaar = models.IntegerField(_('Aadhaar No.'), blank=False)
    phone = models.IntegerField(_('Mobile No.'), blank=False)
    fullname = models.CharField(_('Name'), blank=False, max_length=100)

    def __str__(self):
        return self.fullname








