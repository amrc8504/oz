from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.conf import settings
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
            attrs={
                "class": "form-control",
                "autofocus": False,
            }
        )
    )

    email = forms.EmailField(
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
    
    access_code = forms.CharField(
        widget = forms.PasswordInput(attrs={"class": "form-control"}),
        label = "Access Code"
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
            "access_code",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.pop(
            "autofocus",
            None
        )
        
    def clean_access_code(self):
        access_code = self.cleaned_data.get("access_code")

        if access_code != settings.REGISTRATION_ACCESS_CODE:
            raise forms.ValidationError("Invalid access code.")

        return access_code


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
        widgets = {
            # "first_name": forms.TextInput(attrs={"class": "form-control"}),
            # "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_picture"]
        widgets = {
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }