from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save

STATUS = [('waiting','Bekliyor'),
          ('buyed','SatinAlindi'),
          ('deleted','Silindi'),]


class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    price = models.FloatField(default=0)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title} price:{self.price}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING)
    session_key = models.CharField(max_length=32,blank=True,null=True)
    items = models.ManyToManyField(ShoppingCartItem,blank=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(max_length=20,choices=STATUS,default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"PK:{self.pk} Total:{self.total_price} Status:{self.status}"
    
    def total_price_update(self):
        if self.status == "waiting":
            total_price = 0
            for item in self.items.all():
                total_price += item.price
            self.total_price = total_price
            self.save()
    
@receiver(post_save, sender=ShoppingCartItem)
def shopping_card_item_receiver(sender,instance,created,*args,**kwargs):
    if created:
        instance.price = instance.product.price
        instance.save()
    last_shopping_cart = instance.shoppingcart_set.last()
    if last_shopping_cart:
        last_shopping_cart.total_price_update()
    #instance.shoppingcart_set.first().total_price_update()

@receiver(m2m_changed,sender=ShoppingCart.items.through)
def shopping_card_receiver(sender,instance,*args,**kwargs):
    instance.total_price_update()
