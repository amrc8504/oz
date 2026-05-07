from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

from .models import UserProfile

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_picture"]
        widgets = {
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }