from django.contrib import admin
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','title','slug','status','gender','updated_at',)
    list_filter = ('status','gender',)
    list_editable = ('status',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','title','price', 'stock', 'category','is_home','status',)
    list_filter = ('status', 'category',)
    list_editable = ('status','is_home',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
