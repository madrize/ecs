from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from product.models import Product

class CartItem(models.Model):
    """
    Model for the Cart Item
        
    """
    owner = models.ForeignKey(User)
    item = models.ForeignKey(Product)
    date_added = models.DateTimeField(default=datetime.now)
    quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.item.title
        
    @property
    def price(self):
        return self.quantity*self.item.price

    def get_absolute_url(self):
        return self.item.get_absolute_url()

    class Meta:
        ordering = ['-date_added']
