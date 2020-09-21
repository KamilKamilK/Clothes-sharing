from django import forms
from django.forms import ModelChoiceField

from charity.models import Category, Donation


class CategoryForm(forms.ModelForm):
    # name = forms.MultipleChoiceField(choices=Category.objects.all())
    # name = forms.ModelChoiceField(queryset=Category.objects.values_list('name', flat=True).distinct())

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.CheckboxSelectMultiple()
        }

    # def __init__(self, *args, **kwargs):
    #     super(CategoryForm, self).__init__(*args, **kwargs)
    #     self.fields['name'] = ModelChoiceField(queryset=Category.objects.all())

    # widgets = {
    #     'categories' : forms.MultipleChoiceField(widget=forms.MultipleChoiceField, choices=Category.objects.all())
    # }



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