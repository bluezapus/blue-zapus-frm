from django.contrib import admin

# Register your models here.
from .models import BookCategory, BookCollection


class viewslug(admin.ModelAdmin):
    readonly_fields = ["slug_book"]


admin.site.register(BookCollection, viewslug)
admin.site.register(BookCategory)
