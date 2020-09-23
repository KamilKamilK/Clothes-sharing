from django.contrib import admin
from .models import Donation, Category, Institution

# Register your models here.

admin.site.register(Category)
admin.site.register(Donation)
admin.site.register(Institution)