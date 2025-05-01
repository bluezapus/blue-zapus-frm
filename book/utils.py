from django.core.paginator import Paginator


def paginate_queryset(request, queryset, view_page):
    paginator = Paginator(queryset, view_page)
    page_number = request.GET.get("page")
    page_objects = paginator.get_page(page_number)

    current_page = page_objects.number
    total_pages = paginator.num_pages
    start_page = max(current_page - 1, 1)
    end_page = min(current_page + 2, total_pages)
    custom_page_range = range(start_page, end_page + 1)

    return page_objects, custom_page_range
