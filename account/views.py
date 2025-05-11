from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import RegisterUserForms

# Create your views here.


def register_users(request):
    if request.method == "POST":
        form = RegisterUserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterUserForms()

    context = {
        "title": "BlueZapus",
        "form": form,
    }
    return render(request, "registration/register.html", context)


def LogoutView(request):
    logout(request)
    return redirect("/")
