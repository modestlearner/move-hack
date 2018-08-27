from django import forms
from .models import *
from django.utils.translation import gettext as _
# from django.contrib.auth.models import User


class VehicleAddForm(forms.ModelForm):
    year = forms.IntegerField(widget=forms.TextInput(attrs={'type':'number','class': 'form-control', 'required':True}))
    make = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control'}))



    class Meta:
        model = Vehicle
        fields = ['year', 'make', 'model','plate']


