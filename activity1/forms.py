from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

# The Profile object is in models.py

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profilepicture", "description")
    

