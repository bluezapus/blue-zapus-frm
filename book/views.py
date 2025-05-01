from book.models import BookCollection, BookCategory
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

from book.utils import paginate_queryset

# for searcher
from django.db.models import Q
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    # list_book = BookCollection.objects.all()
    # 'q' for search
    query = request.GET.get("q", "")
    # filtering book
    list_collectionbook = BookCollection.objects.all()

    if query:
        list_collectionbook = (
            list_collectionbook.filter(Q(title__icontains=query)) if query else []
        )

    category_choices = BookCategory.objects.order_by("id")

    # Paginations
    # paginator = Paginator(list_collectionbook, 4)
    # 'not with q search 'paginator = Paginator(BookCollection.objects.all(), 8)
    # page_number = request.GET.get("page")
    # list_book = paginator.get_page(page_number)

    # current_page = list_book.number
    # total_pages = paginator.num_pages

    # start_page = max(current_page - 1, 1)
    # end_page = min(current_page + 2, total_pages)
    # custom_page_range = range(start_page, end_page + 1)

    list_book, custom_page_range = paginate_queryset(
        request, list_collectionbook, view_page=8
    )

    context = {
        "title": "Bz",
        "list_book": list_book,
        "custom_page_range": custom_page_range,
        "category_choices": category_choices,
        "query": query,
    }
    return render(request, "book/index.html", context)


def Category(request, slug_category):
    book_category = BookCollection.objects.filter(
        category__slug_book_category=slug_category
    )
    category_choices = BookCategory.objects.order_by("id")

    # paginator
    list_book, custom_page_range = paginate_queryset(
        request, book_category, view_page=4
    )

    context = {
        "title": "BlueZapus",
        "list_book": list_book,
        "book_category": book_category,
        "custom_page_range": custom_page_range,
        "category_choices": category_choices,
        "slug_category": slug_category,
    }
    return render(request, "book/category.html", context)
