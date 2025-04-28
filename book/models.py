from django.db import models
from django.utils.text import slugify


# Create your models here.
class BookCategory(models.Model):
    title = models.CharField(max_length=250)
    slug_book_category = models.SlugField(blank=True, editable=False)
    description = models.CharField()
    # tags

    def save(self, *args, **kwargs):
        self.slug_book_category = slugify(self.title)
        return super(BookCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BookCollection(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(
        BookCategory, on_delete=models.CASCADE, related_name="books"
    )
    cover_img = models.ImageField(upload_to="book_covers/")
    file = models.FileField(upload_to="books/")
    slug_book = models.SlugField(blank=True, editable=False)
    # tag
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_book = slugify(self.title)
        return super(BookCollection, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
