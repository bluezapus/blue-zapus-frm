from django.contrib import admin

# Register your models here.
from .models import BookCategory, BookCollection


class slugbook(admin.ModelAdmin):
    readonly_fields = ["slug_book"]


class slugbookcat(admin.ModelAdmin):
    readonly_fields = ["slug_book_category"]


admin.site.register(BookCollection, slugbook)
admin.site.register(BookCategory, slugbookcat)
