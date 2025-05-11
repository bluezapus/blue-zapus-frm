from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


# Register your models here.
# decorator
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = [
        "email",
    ]
    list_display = ["email", "name", "is_active", "is_staff"]

    fieldsets = (
        (
            None,
            {
                "fields": (["email", "password"]),
            },
        ),
        (
            "Personal Info",
            {
                "fields": (["phone", "birth", "birthplace"]),
            },
        ),
        (
            "Permissions",
            {
                "fields": (["groups", "is_active", "is_staff", "is_superuser"]),
            },
        ),
    )

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["name", "email", "phone", "password1", "password2"],
            },
        ),
    ]


# admin.site.register(User, UserAdmin)
