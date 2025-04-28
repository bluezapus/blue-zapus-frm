from book.models import BookCollection
from django.shortcuts import render

# Create your views here.


def index(request):
    list_book = BookCollection.objects.all()
    context = {
        "title": "Bz",
        "list_book": list_book,
    }
    return render(request, "book/index.html", context)


# def detail(request, slug_book):
#     read_book = BookCollection.objects.get(slug_book=slug_book)
#     context = {
#         "read_book": read_book,
#     }

#     return render(request, "book/detail.html", context)
