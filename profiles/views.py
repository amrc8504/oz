from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import (
    UserUpdateForm,
    ProfileUpdateForm,
    RegisterForm,
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
            return redirect("dashboard:home")
    else:
        form = RegisterForm()

    return render(request, "profiles/register.html", {"form": form})