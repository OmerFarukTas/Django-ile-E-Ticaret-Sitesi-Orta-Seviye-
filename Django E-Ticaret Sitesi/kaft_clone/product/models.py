from django.db import models
from django.utils.text import slugify
from page.models import DEFAULT_STATUS,STATUS

GENDER = [('man','Erkek'),
          ('woman','Kadin'),
          ('unisex','Unisex'),]
           

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True,max_length=200,editable=False)
    status = models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10,)
    gender = models.CharField(max_length=10,default='unisex',choices=GENDER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title +'('+ self.gender+')'
    
    def save(self,*args,**kwargs):
        if self.gender == 'unisex':
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.gender +'-'+ self.title)
        super().save(*args,**kwargs)
        

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    slug = models.SlugField(null=True,max_length=200,editable=False)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="page",null=True,blank=True)
    status = models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10,)
    price = models.FloatField()
    is_home = models.BooleanField(default=False)
    stock = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.title}({self.category})"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
