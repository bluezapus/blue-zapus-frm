from django.urls import path, include
from . import views

app_name = "book"
urlpatterns = [
    # path("book/<slug:slug_book>/", views.detail, name="book_detail"),
    path("", views.index, name="book_index"),
]
