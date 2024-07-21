from django.db import models
from django.utils.text import slugify

DEFAULT_STATUS = "draft"

STATUS = [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True,max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="page",null=True,blank=True)
    status = models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to="carousel",null=True,blank=True)
    status = models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
