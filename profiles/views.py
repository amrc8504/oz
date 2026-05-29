from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib import messages
from .forms import (
    UserUpdateForm,
    ProfileUpdateForm,
    RegisterForm,
    LoginForm,
)


@login_required
def profile(request):

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.userprofile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            return redirect("profiles:profile")

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=request.user.userprofile
        )

    return render(
        request,
        "profiles/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        }
    )

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Account created successfully.")

            return redirect("dashboard:home")
        else:
            messages.error(request, "Something went wrong. Please check the form and try again.")
    else:
        form = RegisterForm()

    return render(request, "profiles/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Invalid username or password. Please try again."
        )
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(
            self.request,
            "Logged in successfully."
        )
        return super().form_valid(form)