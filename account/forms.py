from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "phone",
            "password1",
            "password2",
        ]
