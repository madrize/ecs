from django.db import models
from django.db.models import permalink
from ecs.settings import STATIC_URL

import datetime
import os

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    #@permalink
    def get_absolute_url(self):
        return "/category/%s/" % self.slug
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "categories"


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.title
    
    #@permalink
    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)
    
    class Meta:
        ordering = ['title']


class ProductManager(models.Manager):
    """ Returns a query set of active products """
    def get_query_set(self):
        return super(ProductManager,self).get_query_set().filter(is_active=True)


class Product(models.Model):
    title = models.CharField("product title",max_length=100)
    slug = models.SlugField(unique=True)
    quantity = models.IntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    
    # tag and categories
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    
    # meta tags for seo
    meta_keywords = models.CharField("Meta Keywords",max_length=255)
    meta_description = models.CharField("Meta Description",max_length=255)
    
    # image files for product
    image = models.ImageField(upload_to="static/images/products")
    thumbnail = models.ImageField(upload_to="static/images/products/thumbnails")
    
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    
    # ratings
    votes = models.PositiveIntegerField("Number of votes",default=0)
    total_rating = models.PositiveIntegerField("Total points",default=0)
    
    # manager
    objects = models.Manager()
    active = ProductManager()
    
    def __unicode__(self):
        return self.title
    
    #@permalink
    def get_absolute_url(self):
        return "/product/%s/" % self.slug
    
    @property
    def rating(self):
        return "%d" % (self.total_rating // self.votes )
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "products"
