from django import forms
from django.forms import ModelChoiceField

from charity.models import Category, Donation

class AjaxForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["quantity",
                  "categories",
                  "institution",
                  "address",
                  "phone_number",
                  "city",
                  "zip_code",
                  "pick_up_date",
                  "pick_up_time",
                  "pick_up_comment",
                  "user"]