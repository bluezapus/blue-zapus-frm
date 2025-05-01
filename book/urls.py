from django.urls import path, include
from . import views

app_name = "book"
urlpatterns = [
    # path("search/", views.search_books, name="search_books"),
    # path("book/<slug:slug_book>/", views.detail, name="book_detail"),
    path("category/<slug:slug_category>/", views.Category, name="book_category"),
    path("", views.index, name="book_index"),
]
