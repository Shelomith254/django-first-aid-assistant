from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': ' '})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ' '})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '})
    )

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")