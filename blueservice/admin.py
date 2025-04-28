from django.contrib import admin

# Register your models here.
from .models import Developer, Service, Category


class serviceadmin(admin.ModelAdmin):
    readonly_fields = ["slug_serv"]


admin.site.register(Service, serviceadmin)
admin.site.register(Category)
admin.site.register(Developer)
