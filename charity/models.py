from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# TYPES = {
#     1: 'Fundacja',
#     2: 'Organizacja pozarządowa',
#     3: 'Zbiórka lokalna'
# }


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, blank=False)


class Institution(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    #  It is also possible to make use of the Enum Functional API with the caveat that labels are automatically generated
    type = models.IntegerField('type', 'Fundacja Organizacja pozarządowa Zbiórka lokalna ')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField(null=False, blank=False)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    adress = models.TextField(max_length=256, null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField(max_length=128, null=False, blank=False)
    zip_code = models.CharField("zip code", max_length=5, default="00-000", blank=True, null=True)
    pick_up_date = models.DateField(null=False, blank=False, default=datetime.date)
    pick_up_time = models.TimeField(null=False, blank=False, default=datetime.time)
    pick_up_comment = models.TextField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
