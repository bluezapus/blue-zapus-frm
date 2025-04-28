from django.urls import path
from . import views

app_name = "service"
urlpatterns = [
    path("detail/<slug:slug_serv>", views.detail, name="service_detail"),
    path("", views.index, name="service_index"),
]
