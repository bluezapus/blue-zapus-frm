from enum import EnumDict
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug_category = models.SlugField(blank=True, editable=False)
    icons = models.ImageField(blank=True, default="category.png", upload_to="category")

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Developer(models.Model):
    name = models.CharField(max_length=50)
    slug_dev = models.SlugField(blank=True, editable=False)
    dev_img = models.ImageField(
        blank=True, default="developer.png", upload_to="developer"
    )

    def save(self, *args, **kwargs):
        self.slug_dev = slugify(self.title)
        return super(Developer, slef).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    develop = models.ForeignKey(Developer, on_delete=models.CASCADE)
    title = models.CharField(max_length=260)
    fill = models.TextField()
    images = models.ImageField(blank=True, default="article.png", upload_to="service")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug_serv = models.SlugField(blank=True, editable=False)
    # tag
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_serv = slugify(self.title)
        return super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
