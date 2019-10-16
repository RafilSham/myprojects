from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [""]

class ImageUploadForm(forms.Form):
    image = forms.ImageField()