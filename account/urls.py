from django.urls import path
from django.contrib.auth.views import LoginView

app_name = "app_account"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
]
