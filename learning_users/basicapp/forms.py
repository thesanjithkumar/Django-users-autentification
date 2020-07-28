from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        # portfolio = forms.URLField(required = False)
        # profilepic = forms.ImageField(required = False)
        model = UserProfileInfo
        fields = ('portfolio', 'profilepic')
