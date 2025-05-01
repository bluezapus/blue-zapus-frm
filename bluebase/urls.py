from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("service/", include("blueservice.urls")),
    path("about/", include("about.urls")),
    path("contact/", include("contact.urls")),
    path("book/", include("book.urls")),
    # registration
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
