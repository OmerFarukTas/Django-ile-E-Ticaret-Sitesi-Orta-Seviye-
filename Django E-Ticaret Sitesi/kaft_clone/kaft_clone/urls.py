from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from page import views
from product.views import category_show
from cart.views import shopping_cart_item_add,go_shopping_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('manage/',views.manage_list,name='manage_list'),
    path('<slug:category_slug>/',category_show,name='category_show'),

    #Page
    path('page/<slug:slug>',views.page_show,name="page_show"),
    path('manage/page_list',views.page_list,name='page_list'),
    path('manage/page_create',views.page_create,name='page_create'),
    path('manage/page_update/<int:pk>/', views.page_update, name='page_update'),
    path('manage/page_delete/<int:pk>/', views.page_delete, name='page_delete'),

    #Carousel
    path('manage/carousel_list/', views.carousel_list, name='carousel_list'),
    path('manage/carousel_create/', views.carousel_create, name='carousel_create'),
    path('manage/carousel_update/<int:pk>/', views.carousel_update, name='carousel_update'),
    path('manage/carousel_delete/<int:pk>/', views.carousel_delete, name='carousel_delete'),

    #Cart
    path('cart/add/<int:cart_item_id>/',shopping_cart_item_add,name="shopping_cart_item_add"),
    path("cart/shopping_cart/<int:pk>", go_shopping_cart,name="shopping_cart"),
]
 
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)