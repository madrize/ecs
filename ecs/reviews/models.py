from django.db import models
from datetime import datetime
from product.models import Product
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date_added = models.DateTimeField(default=datetime.now)
    product = models.ForeignKey(Product)
    sender = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/review/%s/' % (self.slug)
