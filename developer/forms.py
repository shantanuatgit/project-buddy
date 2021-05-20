from .models import *
from django import forms

class AllProfileForm(forms.ModelForm):
    class Meta:
        model=AllProfile
        fields="__all__"
class ImageForm(forms.ModelForm):
    class Meta:
        model=AllProfile
        fields=['profile_pic']
